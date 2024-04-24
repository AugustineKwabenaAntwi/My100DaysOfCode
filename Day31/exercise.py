class Teacher:
    def __init__(self,name):
        self.name = name
    def display_prof(self):
        print(f'My name is {self.name}. I am a {type(self).__name__}')

    def teach(self):
        print('I can teach')    

class Student:
    def __init__(self,name):
        self.name = name
    def display_prof(self):
        print(f'My name is {self.name}. I am a {type(self).__name__}')

    def stud(self):
        print('I can study a lot')

class Youtuber:
    def __init__(self,name):
        self.name = name
    def display_prof(self):
        print(f'My name is {self.name}. I am a {type(self).__name__}')

    def tuber(self):
        print('I can teach and study a lot')
  
class Person(Youtuber,Teacher,Student):
    pass

coder = Person('Kwame')
coder.display_prof()
coder.teach()
coder.stud()
coder.tuber()