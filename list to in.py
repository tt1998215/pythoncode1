from functools import  reduce
def fn(x,y):
    return x*10+y
def ir(L=[]):
    n=int(input("共有几位数？"))
    for i in range(n):
        print('输入第%d位数'%(i+1))
        l=int(input())
        L.append(l)
    return L


A=ir()
a=reduce(fn,A)
print(a)