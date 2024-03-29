a=int(input('enter number'))
A=[]
while a:
    if(a>=5):
        A.append(a)
        a-=1
    if a<5:
        break
print(A)