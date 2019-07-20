def f(x):
    x=x**2
    return x
k=[x for x in range(10)]
a=map(f,k)
print(list(a))