#python arrys 
from array import *
from ctypes import sizeof
ar=array("i",[1,2,3,4,5])
x=len(ar)
c=0
for i in  range (x) :
    c = ar[i]*c
print(c)