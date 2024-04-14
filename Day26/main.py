class HashTable:
    def __init__(self):
        self.MAX = 100 #base value
        self.arr = [None for i in range(self.MAX)]

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

    



t = HashTable()
t['march 7']=130
print(t['march 7'])
