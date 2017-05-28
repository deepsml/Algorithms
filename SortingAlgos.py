"""
Written the 25th of May.

@author: Tarek Samaali

"""

################# swap function #######################
def exchange(array,i1,i2):
		array[i1],array[i2]=array[i2],array[i1]
		
################## Selection Sort ######################

def selection_sort(sublist):
	i,j=0,1
	for i in range(len(list)-1):
		minimum=i
		for j in range(i+1,len(list)):
			if list[minimum]>list[j]:
				minimum=j
		exchange(list,i,minimum)
	return sublist


#################### Gnome Sort #########################
def gnome_sort(list):
	pos=1
	while(pos<len(list)):
		if list[pos]>=list[pos-1]:
			pos+=1
		else :
			exchange(list,pos,pos-1)
			if pos>1 :
				pos-=1
	return list


##################### Bubble Sort ########################

def bubble_sort(list):
	count=len(list)
	while count>0 :
		pos=1
		while pos<count :
			if list[pos]<list[pos-1]:
				exchange(list,pos,pos-1)
			pos+=1
		count-=1
	return list


####################### Quick Sort #######################

def quick_sort(list):

	def quick_sort_recursive_partitions(list,beginning,end):

		def recursive_partitions(list,beginning,end):
			# def debug(list,first,last):
			# 	return list[first:end]

			#### print debug(list,beginning,end)

			# beginning acting as a first pivot
			value_of_pivot=list[beginning]

			item_from_the_left=beginning+1
			item_from_the_right=end

			FLAG = False

			while not FLAG :

				while value_of_pivot<=list[item_from_the_right] and item_from_the_right>=item_from_the_left:
        
					#print list[item_from_the_right] , 'right'
					item_from_the_right-=1

				while value_of_pivot>=list[item_from_the_left] and item_from_the_right>=item_from_the_left:

					#print list[item_from_the_left] , 'left'
					item_from_the_left+=1

				if item_from_the_right<item_from_the_left:
					FLAG = True

				else :
					exchange(list,item_from_the_right,item_from_the_left)

			exchange(list,item_from_the_right,beginning)

			return item_from_the_right

		if beginning<end :
			
			split_point = recursive_partitions(list,beginning,end)
			
			quick_sort_recursive_partitions(list,beginning,split_point-1)
			quick_sort_recursive_partitions(list,split_point+1,end)


	quick_sort_recursive_partitions(list,0,len(list)-1)
	return list


##################### Shell Sort ##################

def shell_sort(array):

	sublist_possibilities=len(array)/4
	pace=len(array)/sublist_possibilities

	array_sublist=[]
	for i in range(pace):
		array_sublist.append(selection_sort(array[i::pace]))

	result=[]
	for el in zip(*array_sublist):
		result.extend(selection_sort([element for element in el]))
	return result


################### Merge Sort ####################

def merge_sort(list):

	def merge_sort_recursive(list):
		if not list or len(list)==1 :
			return list

		mid=len(list)/2
		begin_half=list[:mid]
		ending_half=list[mid:]
		merge_sort_recursive(begin_half)
		merge_sort_recursive(ending_half)

		return selection_sort(begin_half+ending_half)
	merge_sort_recursive(list)
	return list


############### Comb Sort #################

def comb_sort(list,rate):
	#### let us fix a reduction rate that is slightly superior to 1
	length=len(list)
	alpha = length*rate
	changed1 = False
	changed2 = False
	gap=length

	while not(changed1 or changed2) :
  
		changed1=False
		changed2=True
		gap=int(gap/alpha)
		if gap <1: gap=1
		for i in range(0,len(list),gap):
    
			try :
				if list[i]>list[i+gap] :
					exchange(list,i,i+gap)
					changed2=False
			except IndexError:
				pass
	return list


############### Oleyami Sort ################

def oyelami_sort(list):

	def first_fix(list):
		begin,end=0,len(list)-1
		while begin<=end :
			if list[end]<list[begin]:
				exchange(list,end,begin)
			begin+=1
			end-=1
		return list

	list=first_fix(list)
	direction,not_changed,top,bottom=1,False,len(list),0
  
	while not not_changed:
  
		not_changed=True
		if direction==1 :
			count=1
			while count<top :
      
				if list[count]<list[count-1]:
					not_changed= False
					exchange(list,count,count-1)
				count+=1
        
		else :
			count=len(list)-2
			while(count>bottom) :
      
				if list[count]>list[count+1]:
					not_changed= False
					exchange(list,count,count+1)
				count-=1
        
		direction*=-1
		if direction == 1 :
			top-=1
			bottom+=1
	return list
  
################# Counting Sort ####################

def counting_sort(list):
	
	maximum=max(list)
	count=range(maximum)
	occurences=[0]*(maximum+1)
	result=[0]*len(list)
	
	for i in range(maximum):
		occurences[i]+=list.count(i)
		
	for i in range(1,maximum):
		occurences[i]+=occurences[i-1]

	for el in list[::-1]:
			occurences[el]-=1
			result[occurences[el]]=el
			
	return result

################# Radix Sort #######################

def radix_sort(list):

	coef=1
	determine_elements=lambda integer,coef : (integer%10**(coef))/10**(coef-1)
	result=[0]*len(list)
	
	while True:
		input_list=[(lambda x:determine_elements(x,coef))(x) for x in list]
		back_input_list=input_list[::-1]
		back_list=list[::-1]
		
		if all(not el for el in input_list):
			break

		count=[0]*10
		
		for i in range(len(count)):
			count[i]+=input_list.count(i)

		for i in range(1,len(count)):
			count[i]+=count[i-1]
		

		for i in range(len(back_input_list)):
			count[back_input_list[i]]-=1
			result[count[back_input_list[i]]]=back_list[i]
		
		list=result
		coef+=1

	return list

##################### Bucket Sort ###################

def bucket_list(list):

	def calculate_position(value,number_of_values,maximum_value):
		return int(value*number_of_values/(maximum_value+1))

	number_of_values=len(list)
	maximum_value=max(list)
	buckets=[[] for _ in range(number_of_values)]

	for element in list:
		position_in_buckets=calculate_position(element,number_of_values,maximum_value)
		buckets[position_in_buckets].append(element)
		buckets[position_in_buckets]=selection_sort(buckets[position_in_buckets])
		
	result=[]
	for el in buckets:
		result.extend(el)

	return result

