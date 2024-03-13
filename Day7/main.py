
class Employee:

    def __init__(self,_id,_name):#initializing the properties
        self.name = _name
        self.id = _id

    def output(self):
        print(f'Id:{self.id}\nName:{self.name}')


emp1 = Employee(445,"Kwame") #emp is an object of the type/class Employee 
emp2 = Employee(223,"Kwasi")

emp2.output()

#deleting property/attribute id

del emp2.id
# using error handling because it will throw an error after deleting ID
emp2.output()

