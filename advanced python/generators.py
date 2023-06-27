###Generators and Iterators: Generators are functions that can be paused and resumed, allowing you to generate a sequence of values over time.
# They are memory-efficient and useful for working with large data sets. 
# Iterators are objects that implement the iterator protocol, allowing you to loop over a collection of items.
# Generators:

# Generators are special functions that use the yield keyword instead of return to return values one at a time.
# When a generator function is called, it returns a generator object. The generator object can be iterated over to retrieve the values produced by the generator function.
# Generators are memory-efficient because they generate values on-the-fly instead of storing them in memory.
# They are particularly useful when dealing with large data sets or when the entire sequence of values cannot be determined in advance.
# Here's an example of a generator function that generates Fibonacci numbers:

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a,b = b, a+b
        
fib = fibonacci()
for i in range(10):
    print(next(fib))