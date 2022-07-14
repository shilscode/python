from ctypes import sizeof

stri =12345
i=0
s=0
for i  in range(5):
            p=stri%10
            s=s*10+p
            stri=stri//10
print(s)