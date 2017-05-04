class Fib(object):
    def __init__(self):
        self.a,self.b=0,1#初始化两个计数器
    def __iter__(self):
        return self   #实例本身为迭代对象
    def  __next__(self):
       self.a,self.b=self.b,self.a+self.b
       if self.a>10000:
           raise StopIteration
       return self.a
    def __getitem__(self, n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
            return a


for  n in Fib():
    print(n)

print(Fib()[6])


