import os,sys

path='/home/ts/code'
X=[x for x in os.listdir(path) if os.path.isdir(x)]
print(X)