#Read me
#What is class, object and method?
#Think of a class as a blueprint or a plan for creating things. Let's say we have a class called "Animal." The Animal class tells us what an animal should have, like how many legs it has, what it eats, and how it moves.
#Now, an objects is like a real animal that we create based on that blueprint. So, if we use the Animal class, we can create objects like a dog, a cat, or a bird. Each of these objects will have its own characteristics, like a dog with four legs, eats bones, and runs.
#Finally, a method is like a special action that an animal can do. For example, in the Animal class, we might have a method called "makeSound." So, the dog object can use the "makeSound" method to bark, the cat object can use it to meow, and the bird object can use it to chirp.
#In simple terms, a class is a plan, an object is something created based on that plan, and a method is a special action that the object can do.
# Define a class called "Animal"
class Animal:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says: Woof woof!")


    def meow(self):
        print(self.name + " says: Meow meow!")

# Create an object (instance) of the Animal class
my_dog = Animal("Buddy")
my_cat = Animal("Pusa")


# Call the bark() method of the my_dog object
my_dog.bark()
my_cat.meow()

# Define a function called "add_numbers"
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

# Call the add_numbers function and store the result in a variable
result = add_numbers(3, 5)

# Print the result
print("The sum of 3 and 5 is:", result)
