from tkinter import Tk,Button,Label,PhotoImage,Entry



def show_second():
    page2=Tk()
    page2.title('به کلاس پایتون خوش آمدید')
    page2.geometry('500x500')
    page2.resizable(width=False,height=False)
    page2.configure(bg='red')
    page2.mainloop()

page=Tk()

page.title('به کلاس پایتون خوش آمدید')
page.geometry('600x700')
page.resizable(width=False,height=False)
page.configure(bg='gold')

name=Label(page,text='نام خود را وارد کنید')
name.pack(side='top',fill='x',expand='yes')

txtName = Entry(page, bd = 5,font=('B mitra',14))
txtName.pack(side='right')

btnMsg=Button(page,text='نمایش صفحه 2',fg='red',bg='white',font=20,activebackground='black',command=show_second)
btnMsg.pack(side='left')


mypic=PhotoImage(file='1.png')
lblpic=Label(page,image=mypic)
lblpic.image=mypic
lblpic.place(x=300,y=10)







page.mainloop()