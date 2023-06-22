# dictionaries -> key-value pairs, unordered, mutable

# create a dictionary   
my_dict = {}

print(my_dict)

# create a dictionary with values
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)

# add a key-value pair
my_dict[3] = 'cat'
print(my_dict)

print(my_dict[1])

#access list of keys
print(my_dict.keys())

def dict_keys(my_dict) -> list:
    return [key for key in my_dict]
def dict_values(my_dict) -> list:
    return [my_dict[key] for key in my_dict]

print(dict_keys(my_dict))
print(dict_values(my_dict))

# methods

# 1. deletion

print(my_dict.pop(1)) # returns the value of the key

print(my_dict.popitem()) # returns the key-value pair

print(my_dict.clear())

# 2. update

print(my_dict.update({1: 'apple', 2: 'ball'}))
print(my_dict)

# 3. copy

print(my_dict.copy())

# 4. fromkeys

print(my_dict.fromkeys([1, 2, 3], 'apple'))

# 5. get

print(my_dict.get(1))