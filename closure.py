def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper



@log    #本身是一个闭包，必须调用才能返回值
def happy_sum(*args):
    def sum():
        ax=0
        for i in args:
            ax=ax+i
        return ax
    return sum

happy_sum(1,2,3,4,5,6,7)



