class FatherClass(object):
    def __init__(self):
        self.name=777
    __slots__ = ('name','sex')

class Son(FatherClass):
    __slots__ = ('age', 'grades')

class Gson(Son):
    __slots__ = ('a','b')

# s=Son()
# s.secret=123
# print(s.secret)
s=Gson()
s.name=999
print(s.name)