# lambda functions are anonymous functions that are used to perform simple tasks
'''
 --------------------->[Syntax]<---------------------
    lambda arguments : expression
    --------------------------------------------------
    lambda functions are anonymous functions that are used to perform simple tasks
    lambda functions are also called anonymous functions because they do not have a name 
    lambda functions are usually used for one line functions 
'''

x = lambda a : a + 10
print(x(5))

# lambda functions can take multiple arguments
x = lambda a , b : a * b
print(x(5 , 6))

# lambda functions can be used inside other functions
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

