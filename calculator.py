a  = float (input("enter first  number  :"))
op = input("enter operator(+,-,*,%,/,//,%)  :")
b  = float (input("enter second number  :"))

if  op == "+":
    print(a+b)
elif  op == "-":
    print(a-b)
elif  op == "*":
    print(a*b)    
elif  op == "/":
    print(a/b)    
elif  op == "%":
    print(a%b)        
else :
    print("invalid operation")   