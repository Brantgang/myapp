from functools import reduce

def str2flaot(x,y,z):
    f= lambda x,y,z:x+y+z
    return f(x,y,z)

#------reduce-第二题
#存在疑问？
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str3float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

#filter
def is_odd(x):
    return x%2==1

def is_palidhome(n):
    return str(n)==str(n)[::-1]
#sorted
def by_name(n):
    return n[0]
def by_num(b):
    return b[1]
#partical
#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
import functools
int2=functools.partial(int,base=2)
print(int2('10001'))


