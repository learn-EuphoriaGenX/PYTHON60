class Animal:
    def walk(self):
        print("Animal is walking")

class Dog(Animal):
    def walk(self): # Method overriding
        print("Dog is walking")

class Cat(Animal):
    def walk(self): # Method overriding
        print("Cat is walking")

class Bird(Animal):
    def walk(self): # Method overriding
        print("Bird is walking")

dog = Dog()
cat = Cat()
bird = Bird()


for animal in (dog, cat, bird):
    animal.walk()  # Polymorphic behavior: same method name, different implementations