class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('Woof! Woof!')
        
        
        
dog = Dog('Fido', 2)
print(dog)
print(dog.name)
print(dog.age)  