
from tkinter import Tk,Button,Label,PhotoImage,Entry,messagebox



def showmsg():
    lblmsg=Label(page,text=txtName.get()+' به کلاس خوش آمدید',bg='orange',fg='black',font=('B mitra',30),)
    lblmsg.pack()

def showpic():
    mypic=PhotoImage(file='1.png')
    lblpic=Label(page,image=mypic)
    lblpic.image=mypic
    lblpic.pack(side='bottom')

def destroy_form():
    if messagebox.askyesnocancel('خروج','آیا میخواهید خارج شوید'):
        page.destroy()


page=Tk(className='vira')
page.title('به کلاس پایتون خوش آمدید')
page.geometry('600x700')
page.resizable(width=False,height=False)
page.configure(bg='pink')


lbl=Label(page,text="نام خود را وارد کنید",bg='lightblue',fg='black',font=('B mitra',20),)
lbl.pack(side='top',fill='both')

txtName = Entry(page, bd = 5,font=('B mitra',20))
txtName.pack(side='top',fill='both')

btnMsg=Button(page,text='نمایش پیام',fg='red',bg='aqua',font=('B mitra',30),activebackground='black',command=showmsg)
btnMsg.pack(side='top',fill='both')


btnMsg=Button(page,text='نمایش عکس',command=showpic,bg='lightblue',fg='black',font=('B mitra',30))
btnMsg.pack(side='top',fill='both')

exit_btn= Button(page, text='exit', fg='black', bg='red',command=destroy_form,font=('B mitra',30))
exit_btn.pack(side='top',fill='both')




page.mainloop()