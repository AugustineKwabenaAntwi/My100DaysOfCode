class Employee:
    def __init__(self,_id,_name):#initializing the properties
        self.name = _name
        self.id = _id

    def output(self):
        print(f'Id:{self.id}\nName:{self.name}')


emp = Employee(445,"Kwame") #emp is an object of the type/class Employee 
emp.output()
#unfinished
