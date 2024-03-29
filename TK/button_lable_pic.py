import tkinter as tk
from tkinter import Tk,Button,Label
frm=Tk(className='vira')
frm.title('به کلاس پایتون خوش آمدید')
frm.geometry('600x700')
frm.resizable(width=False,height=False)
frm.configure(bg='gold')


b1=Button(frm,text='click 1',fg='black',bg='lightgreen',font=('Arial',30),activebackground='lightblue').grid()
b2=Button(frm,text='click 2',fg='black',bg='#4a7a8c',font=30,activebackground='yellow').grid(row=0,column=1)
b3=Button(frm,text='click 3',fg='black',bg='white',font=30,activebackground='yellow').grid(row=0,column=2)
b4=Button(frm,text='click 4',fg='black',bg='white',font=30,activebackground='yellow').grid(row=0,column=10)

l=Label(image=tk.PhotoImage('1.png')).grid()


frm.mainloop()