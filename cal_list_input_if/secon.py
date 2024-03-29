Data=input("enter your phrase  = ").split()

s=0
a=int(Data[0])
oprator=Data[1]
b=int(Data[2])

if oprator=='+':
    s=a+b
if oprator=='-':
    s=a-b
elif oprator=='*':
    s=a*b
elif oprator=='**':
    s=a**b
elif oprator=='/' and b!=0:
    s=a/b
else:
    print("error")
print("result is  ==",s)
