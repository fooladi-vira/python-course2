file=open('myfile.txt','r')
contacts=file.readlines()
while True:
    txt=input(" pls enter name for search number or exit =  ")
    if txt!='exit':
        list=[]
        for l in contacts:
            if l.rfind(txt)!=-1:
                print(l)   
        else:
            print(' not found')
    else:
        print(" thanks for use my APP")  
        file.close()  
        break

        


    
