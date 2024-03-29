file=open('myfile.txt','a')
dic_contact={}
while True:
    text=input('name and number  or exit  ')
    if text=='exit':
        break
    else:
        name,number=text.split()
        dic_contact[name]=number
        print(" record to dict")
        

for item in dic_contact.items():
    file.write('\n'+6*'*'+'\n')
    file.write(item[0]+'>>>>>>'+item[1])

file.close()
