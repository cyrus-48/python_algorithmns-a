# Decorators: Decorators are a way to modify the behavior of functions or classes in Python. 
# They allow you to wrap a function or class with additional functionality without permanently modifying the original code.import time

import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def my_function():
    for _ in range(1000):
        print("Hello World!")

my_function()
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
