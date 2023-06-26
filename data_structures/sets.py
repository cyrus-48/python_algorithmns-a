# sets > is an unordered collection of unique elements that is mutable anf does not allow any duplicates 

my_set = set()

#adding elements to a set
my_set.add(1)
print(my_set)

#adding multiple elements to a set

my_set.update([2,3,4,5])
print(my_set)

# removing elements from a set
my_set.remove(1) # throws an error if the element is not present in the set
print(my_set)

my_set.discard(2) # does not throw an error if the element is not present in the set    

# union of sets

my_set1 = {1,2,3,4,5}
my_set2 = {4,5,6,7,8}

print(my_set1.union(my_set2))

# intersection of sets
my_set1 = {1,2,3,4,5}
my_set2 = {4,5,6,7,8}
print(my_set1.intersection(my_set2))    

# difference of sets
my_set1 = {1,2,3,4,5}
my_set2 = {4,5,6,7,8}
print(my_set1.difference(my_set2))

# symmetric difference of sets >> elements that are in either of the sets but not in both
my_set1 = {1,2,3,4,5}
my_set2 = {4,5,6,7,8}
print(my_set1.symmetric_difference(my_set2))


