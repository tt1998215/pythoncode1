# import functools
# def log(func):
#     # @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print("begin call %s():"%func.__name__)
#         res=func(*args,**kw)
#         print("the result of the program is {}".format(res))
#         print("end call %s():"%func.__name__)
#         #resturn res
#     return wrapper
#
# @log
# def f2(x,y):
#     return x+y
#
# def main():
#     f2(4,6)
#     print("the name of the function is :"+f2.__name__)
#
# main()
import sys
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
if __name__=='__main__':
    test()
