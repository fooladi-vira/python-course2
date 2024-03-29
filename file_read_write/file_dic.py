print('hello')

name=input('enter file:')
handle=open(name)
counts=dict()
large=-1
for line in handle:
    #print('f line)
    line=line.rstrip()
    words=line.split()
    #if words[0]=='I':
        #print(line)

    for word in words:
        old=counts.get(word,0)
        new=old+1
        counts[word]=new

    for k,v in counts.items():
        if v> large:
            large=v
            mostW=k
print(mostW,large)
#print(counts)
