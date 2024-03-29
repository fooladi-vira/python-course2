

def check_avg(avg):
    status=''
    if avg >17 and avg<=20:
       status="Graet"
    if avg<=17 and avg >=10:
        status="Good"
    if avg <10 and avg>=0:
        status="Bad"
    elif avg<0 or avg>20:
        status='IDK'
    return status

Dict={}
while True:
    name=input(" please enter name or exit---> ")
    if name=='exit':
       break
    avg=float(input(" please enter avg --> "))
    code=int(input(" please enter student number   >>>>"))
    Dict[(name,code)]=avg
for p  in Dict:
    avg=Dict[p]
    s=check_avg(avg)
    print(p,f'your sattus  of {avg} is  ',s)


