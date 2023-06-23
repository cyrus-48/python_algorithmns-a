# tuples - immutable lists
# tuples are the same as lists, but they are immutable

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

#Accesing elemnts in a tuple
for elem in my_tuple:
    print(elem)
    
#Appending elements to a tuple
my_tuple = my_tuple + (6, 7, 8)
print(my_tuple)

# more functions
my_tuple = (1,2,3,4,["one", "two", "three"])
my_tuple[4][0] = "ONE"

print(my_tuple)
 
print(my_tuple.count(1))
print(my_tuple.index(1))
