
# class
class Human:
    name = "Passpass"
    age = 12
    color = "black"

    def __init__ (this, name, age, color):
        this.name = name
        this.age = age
        this.color = color

    def walk(this):
        print(f"{this.name} is Walking...")

    def running(this):
        print(f"{this.name} is Running...")

    def __str__ (this):
        return f'Name: {this.name} | Age: {this.age} | Color: {this.color}'
        
class Dog(Human):
    def walk(self):
        print("Dog is Walking.....")
    

h1 = Human("Ram", 14, "brown")
h2 = Human("Shyam", 15, "white")
# print(h2)
# print(h1)
# h1.walk()
h1.running()
# h2.walk()
# h2.running()

d1 = Dog("jimmy", 12, "black")
d1.walk()



# inheritance
# encapsulation

# Polymorphism
# abstraction





