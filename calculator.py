
a=int(input("enter a integer:"))
b=int(input("enter a integer:"))
c=input("enter a operator [+,-,*,%,/,//,**] :")
if c=='+':
    print("Addition of integers: ",a+b)
elif c=='-':
    print("Subtraction of integers: ",a-b)
elif c=='*':
    print("Product of integers: ",a*b)
elif c=='/':
    print("Division of integers: ",a/b)
elif c=='%':
    print("Remainder of integers: ",a%b)
elif c=='//':
    print("Floor division of integers: ",a//b)
elif c=='**':
    print("Exponentiation of integers: ",a**b)
else :
    print("Invalid operator !!!")


