def read_file(name_file):
    file=open(name_file,'r')
    data=file.readlines()
    return data

def write_file(name_file,data):
    file=open(name_file,'a')
    file.write(data)

def get_data():
    name=input('enter name>>>> ')
    number=input(" number for name>>>")
    return name,number

name_file='contact.txt'
print(" start APP")
# while True:
#     name,number=get_data()
#     if name+number=='exit':
#         break
#     else:
#         data=name+">>>>"+number+'\n'
#         write_file(name_file,data)
#         print("OK")

contact_file=read_file(name_file)
name_search=input("pls enter name for search number>>>")
for x in contact_file:
    if x.rfind(name_search)!=-1:
        print(x)
        break
    else:
        print("not find")