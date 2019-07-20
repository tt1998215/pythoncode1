import  functools
def log(text):
    def decorator(func):
        # @functools.wraps(func)

        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# @log('happy in')
def now():
    print('call %s():' %now.__name__)
now = log('execute')(now)
print(now())