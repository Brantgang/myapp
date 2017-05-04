from com.myfunc import str2flaot
print(str2flaot(3,5,4))
f=lambda a,b,c:a+b+c
print(f(3,2,3))

from com.myfunc import  str3float
print(str3float('0'))
print(str3float('123.456'))
print(str3float('123.45600'))
print(str3float('0.1234'))
print(str3float('.1234'))
print(str3float('120.0034'))
#L=list(filter(is_palidhome,range(0,1000)))
#print(L)
from com.myfunc import by_name
from com.myfunc import  by_num
L=[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
L3 = sorted(L,key=by_num)
print(L3)
print(L2)