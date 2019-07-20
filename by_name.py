def by_name(t):
    return abs(t[1])
L = [('Bob', -75), ('Adam', -92), ('Bart', -66), ('Lisa', -88)]
L2=sorted(L,key=by_name,reverse=True)
print(L2)
# sorted() key 对可以对list中的元素进行处理，但并没有改变原来的list中的元素，只改变了他们的顺序，
#sorted 本身是一个高阶函数，可以使用key调用其他的抽象函数