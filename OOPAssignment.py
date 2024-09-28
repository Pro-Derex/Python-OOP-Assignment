class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am {self.gender}.")


person1 = Person("Ekwuazi Progress", 28, "Male")

person1.introduce()
