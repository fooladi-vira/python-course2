from tkinter import *
from tkinter import messagebox



main_page=Tk()
main_page.title("my music player")
main_page.geometry("700x800")
main_page.configure(bg='aqua')
main_page.resizable(width=False,height=False)





def showmsg():
    lblmsg=Label(frame2,text=' به اپلیکیشن ویرا خوش آمدید',bg='orange',fg='black',font=('B mitra',30),)
    lblmsg.pack()

def showpic():
    mypic=PhotoImage(file='1.png')
    lblpic=Label(frame2,image=mypic)
    lblpic.image=mypic
    lblpic.pack()

def destroy_form():
    if messagebox.askyesnocancel('خروج','آیا میخواهید خارج شوید'):
        main_page.destroy()



var = StringVar()

frame1 = Frame(main_page,width=50,height=50,bg='red',)
frame1.pack(side='top')
frame2 = Frame(main_page,width=50,height=50,background='blue')
frame2.pack(side='top')
frame3 = Frame(main_page,bg='aqua')
frame3.pack(side='top')
frame4 = Frame(main_page,bg='green')
frame4.pack(side='top')
frame5 = Frame(main_page,bg='white')
frame5.pack(side='top')
frame6 = Frame(main_page,bg='yellow')
frame6.pack(side='top')



button1 = Button(frame1,text='frame1',bg='yellow',width=21,font=20,bd=5,padx=10,pady=5,)
button1.pack( side ='left')
button1_2 = Button(frame1,text='frame1_1',width=20,height=2,bd=5,padx=10,pady=5,font=20,)
button1_2.pack( side ='left')
button1_3 = Button(frame1,text='frame1_2',width=15,height=3,bd=5,padx=10,pady=5,font=20,)
button1_3.pack( side ='left')


button2 = Button(frame2,text='frame2',width=40,command=showmsg)
button2.pack( side ='right')

button3 = Button(frame3,text='frame3',width=40,command=showpic)
button3.pack( side ='left')

button4 = Button(frame4,text='frame4',width=40,command=showpic)
button4.pack( side ='left')

button5 = Button(frame5,text='frame5',width=40,command=showpic)
button5.pack( side ='left')


button6 = Button(frame6,text='frame6',width=40,command=showpic)
button6.pack( side ='left')


#mypic=PhotoImage(file='play.png')

# playbutton = Button(frame3,image=mypic,command=showpic)
# playbutton.pack( side ='left')

menubar=Menu(frame1)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = showmsg)
filemenu.add_command(label = "Open", )
filemenu.add_command(label = "Save",)
menubar.add_cascade(label = "File", menu = filemenu)
main_page.config(menu = menubar)






main_page.mainloop()