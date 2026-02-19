class Parent :
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}."
    
    def job(self):
        return "I am a parent and I take care of my family."
    
class Child(Parent):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def job(self):
        return f"I am {self.name} a child age {self.age}  and I go to school."

p1 = Parent("Alice")
print(p1.job())
print(p1.greet())
c1 = Child("Bob", 13)
print(c1.greet())
print(c1.job())