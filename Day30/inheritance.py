class Animal:
    def __init__(self,habitat,sound):
        self.habitat = habitat
        self.sound = sound

    def get_habitat(self):
        print(self.habitat)

    def uniq_sound(self):
        print(f'some animal sound is {self.sound}') 

class Dog(Animal):
    def __init__(self, habitat, sound,color):
        super().__init__(habitat, sound)
        self.color = color

    def shwcolor(self):
        return self.color    

x = Dog("kennel",'woof','green')
print(x.shwcolor())
x.uniq_sound()

