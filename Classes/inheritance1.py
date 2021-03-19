# This class inherits from another class called object. The object class is the base class for all classes in Python.
# The object class have all the magic methods and other classes inherit these methods from the object class.
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Mammal is an Animal. So it inherits all features/methods of Animal class
# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    # When we implement this constructor, it replaces the parent class' constructor (It overrides parent class'
    # constructor). So if dont call for parent class' constructor, we dont get attributes of parent class.(e.g we
    # would not have age attribute in Mammal class)
    def __init__(self):
        # To call the parent class' methods, we can use super() method.
        super().__init__()
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


# m is Animal, Mammal and object
m = Mammal()

print("m is an instance of Mammal:", isinstance(m, Mammal))
print("m is an instance of Animal:", isinstance(m, Animal))
print("m is an instance of object:", isinstance(m, object))

print("Mammal is a subclass of Animal:", issubclass(Mammal, Animal))

print("age:", m.age)
