n=10
a=0
b=1
print(a,"\n",b)
for i in range(3,n+1):
    print(a+b)
    c= a+b
    a=b
    b=c
