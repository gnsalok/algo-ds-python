''' Fibonacci series using iterators '''
class My_Fib():
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.a = 1
        self.b = 1
        return self
    
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

if __name__ == '__main__':
    for f in My_Fib(100):
        print(f)
        