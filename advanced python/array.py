''' 
  --------------------------[arrays/lists]--------------------------
    An array is a collection of items stored at contiguous memory locations. 
    The idea is to store multiple items of the same type together.
    
    python does not have built-in support for arrays, but python lists can be used instead.
    python lists are used to store multiple items in a single variable.
    
    python lists are created using square brackets: []
    
    syntax:
        list_name = [item1 , item2 , item3 , ...]
        
    python lists are ordered, changeable, and allow duplicate values.
    
    methods:
    
    append() - adds an element at the end of the list
    clear() - removes all the elements from the list
    copy() - returns a copy of the list
    count() - returns the number of elements with the specified value
    extend() - add the elements of a list (or any iterable), to the end of the current list
    index() - returns the index of the first element with the specified value
    insert() - adds an element at the specified position
    pop() - removes the element at the specified position
    remove() - removes the item with the specified value
    reverse() - reverses the order of the list
    sort() - sorts the list
    


'''

# case 

# # create a list
fruits = ["apple" , "banana" , "cherry" , "orange" , "kiwi" , "melon" , "mango"]

# # print the list
print(fruits)

## access item in a list
x = fruits[0]
print(x)

## iterate through a list
for x in fruits:
    print(x)
    
## change the value of a list item
fruits[1] = "blackcurrant"
print(fruits)

## check if an item exists in a list
if "apple" in fruits:
    print("yes, apple is in the fruits list")
    
## methods of a list
fruits.append("pineapple")
print(fruits)

fruits.insert(1 , "orange")
print(fruits)

fruits.remove("orange")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

del fruits[0]
print(fruits)

fruits.clear()
print(fruits)

