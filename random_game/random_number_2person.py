import random

def plus(score):
    return score+random.randint(1,10)

p1=str(input('enter your name character 1  >>>'))
p2=str(input('enter your name character 2  >>>'))
Dict_score={p1:[0],p2:[0]}

i=0
while True:
    i+=1
    enter_key=str(input(f' please enter  key {p1}  '))
    if enter_key!= None:
        dice=random.randint(1,6)
        if dice==6:
            Dict_score[p1].append(plus(dice))
            
    else:
        continue
    enter_key=str(input(f'enter your key {p2} '))
    if enter_key!= None:
        dice=random.randint(1,6)
        if dice==6:
            Dict_score[p2].append(plus(dice))
    else:
        continue
    if i>=5:
        break
    
for p,s in Dict_score.items():
    score=sum(Dict_score[p])
    print(f'score of {p} is {score}')
    
    




