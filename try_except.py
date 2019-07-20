# try:
#     print('try...')
#     r=10/2
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('there is a zerodivisionerror')
# finally:
#     print('finally')
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
foo(0)