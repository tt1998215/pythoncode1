from collections import namedtuple,deque
Point = namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(isinstance(p,tuple))
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q) #先进后出是栈使用append和pop即可实现，普通的list就行了
q.popleft()
print(q)