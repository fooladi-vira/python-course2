def add(a,b):
    print(a+b)
    

def sub(a,b):
    print(a-b)

def div(a,b):
    print(a/b)

def mul(a=5,b=10):
    print(a*b)

num1=int(input(" please enter num 1---> "))
num2=int(input(" please enter num 2---> "))
oprand=input(" please enter / or * or + or -  >>>>")

if oprand=='+':
   add(num1,num2)
if oprand=='-':
   sub(num1,num2)
if oprand=='*':
    mul(num1,num2)
if oprand=='/' and num2!=0 :
   div(num1,num2)
