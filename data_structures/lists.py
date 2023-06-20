#list is a pytohn data structure used tostore collectin of items ,, may be of different data types

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)
# adding elements to the list 

# append() method adds the element to the end of the list
my_list.append(12)
print(my_list)

# insert() method adds the element to the specified index
my_list.insert(0,0)
print(my_list)

# extend() method adds the elements of the iterable to the end of the list
my_list.extend([13,14,15])
print(my_list)

# 2. Accessing elements of the list
# indexing and slicing
my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list[0]) # indexing

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list[0:5])# slicing
print(my_list[0:10:2])# slicing with step
print(my_list[::-1])# slicing with step in reverse order
print(my_list[-1])# negative indexing 
print(my_list[-1:-5:-1])# negative slicing 

# 3. deletinf elements in a list 
# pop() method removes the element at the specified index
my_list.pop(0)
print(my_list)

# remove() method removes the first occurence of the element with the specified value
my_list.extend(['python','java','c','c++','c#'])
my_list.remove('python')
print(my_list)

# del keyword removes the element at the specified index
del my_list[0] # remove 2 from the list 
print(my_list)

# clear() method empties the list
my_list.clear() #  empties the whole list
print(my_list)

#other methods in list

# count() method returns the number of elements with the specified value
my_second_list = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1]
my_count = my_second_list.count(1)  
print(my_count) 
# return the number of times 1 appers in the list

# index() method returns the index of the first element with the specified value
my_index = my_second_list.index(1) # returns the index of the first occurence of 1
print(my_index)

# sort() method sorts the list
my_sort = my_second_list
my_sort.sort()
print(my_sort)

# reverse() method reverses the list
my_reverse = my_sort
my_reverse.reverse()
print(my_reverse)

# copy() method returns a copy of the list
my_copy = my_reverse.copy()
print(my_copy)

# len() method returns the length of the list
size = len(my_copy)
print(size)
# min() method returns the smallest element in the list
 

def max_number(my_list: list):
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max
def min_number(my_list: list):
    min = my_list[0]
    for i in my_list:
        if i < min:
            min = i
    return min

minimum = min_number([23,11,23,34,45,56,67,78,89,90])
# max() method returns the largest element in the list
maximum = max_number([23,11,23,34,45,56,67,78,89,90])

print(minimum,maximum)


