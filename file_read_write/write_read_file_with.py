
#myList=['zahra   0912\n','ali   0910\n','ana   0913\n','jak   0914\n','jordan   0910\n5']


def write_file(myList):
    try:
        with open('Mycontact.txt','x') as file:
            print('file created')
    except:
        print('file exist')
        try:
            with open('Mycontact.txt','a') as file:
                file.writelines(myList)
        except:
            print("Something went wrong when writing to the file")
                
       


def read_file(filename):
    try:
        with open(filename,'r') as file:
            print(file.read())
    except:
        print("Something went wrong when reading the file")
    finally:
        print("finish")



def get_data():
    contact=[]
    while True:
        text=input('name and number  or exit  ')
        if text=='exit':
            break
        else:
            contact.append(text+'\n')
            print(" record")
    return(list(contact))
        

write_file(get_data())