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
        self.arr[h] = val

    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]  

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h]=None   

    



t = HashTable()
t['march 7']=130  #the getitem and setitem operators allowed to represent in dictionary form
print(t['march 7'])
