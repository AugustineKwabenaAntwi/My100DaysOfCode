class HashTable:
    def __init__(self):
        self.MAX = 10 #base value
        self.arr = [[] for i in range(self.MAX)]

    '''arr = [None for i in range(10)]
    print(arr)
    output--> [None, None, None, None, None, None, None, None, None, None] '''
    def get_hash(self,key):
        h=0
        for char in key:
            h = h + ord(char)
        return h%self.MAX
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]): #remember this is a nested array--> (idx,[element0,element1])
            if len(element) == 2 and element[0]==key:
                self.arr[h][idx] = (key,val) #2d array
                found = True
                break
        if not found:    
            self.arr[h].append((key,val)) #if key does not exist update key value pair

    def __getitem__(self,key): #list operator
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
                break

    



t = HashTable()
t['march 6'] = 120
t['march 6'] = 90
print(t.arr)
 #the getitem and setitem operators allowed to represent in dictionary form
