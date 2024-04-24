class Fibonacci:
    def __init__(self,limit):
        self.a = 0
        self.b = 1
        self.n = 1
        self.limit = limit

    def __iter__(self):
        return self
    
    def __next__(self):

        if self.n == self.limit:
            raise StopIteration
        else:
            result = self.a + self.b
            self.a = self.b
            self.b = result
            self.n +=1
            return self.b

r= Fibonacci(9)
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))