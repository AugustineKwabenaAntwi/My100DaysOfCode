class Animal:
    def __init__(self,habitat,sound):
        self.habitat = habitat
        self.sound = sound

    def get_habitat(self):
        print(self.habitat)

    def uniq_sound(self):
        print(f'some animal sound is {self.sound}') 

class Dog(Animal):
    def __init__(self, habitat, sound):
        super().__init__(habitat, sound)