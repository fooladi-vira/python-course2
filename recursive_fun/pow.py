import math

def pow(a,b):
  if(b > 0):
    result = a * pow(a,b-1)
  else:
    result = 1
  return result


num1=int(input('enter number1>>>> '))
num2=int(input('enter number2>>>'))
r2=math.pow()
r=pow(num1,num2)
print(r)
