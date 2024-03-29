# تمرین تغییر متن برچسب بر اساس ورودی


from tkinter import Tk,Button,Label,PhotoImage,Entry
def showmsg():
    name['text']=txtName.get()+'*خوش آمدید *'

page=Tk()

page.title('به کلاس پایتون خوش آمدید')
page.geometry('600x500')
page.resizable(width=False,height=False)
page.configure(bg='gold')

name=Label(page,text='نام خود را وارد کنید',font=30)
name.pack(side='top')

txtName = Entry(page, bd = 5,font=('B mitra',20))
txtName.pack(side='top')

btnMsg=Button(page,text='نمایش پیام',fg='red',bg='white',font=30,activebackground='black',command=showmsg)
btnMsg.pack(side='top')

# mypic=PhotoImage(file='1.png')
# lblpic=Label(page,image=mypic)
# lblpic.image=mypic
# lblpic.pack(side='top')

page.mainloop()