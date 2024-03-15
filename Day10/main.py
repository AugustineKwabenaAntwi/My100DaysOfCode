class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show():
        print(f"I dont know what I say")    


class Cat(Pet):
    def __init__(self, name, age,color):
        super().__init__(name,age)
        self.color=color

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. My color is {self.color}")    

class Dog(Pet):
    def __init__(self, name, age,breed):
        super().__init__(name,age)
        self.breed=breed

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. My breed is {self.breed}") 