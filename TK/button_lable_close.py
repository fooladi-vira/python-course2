# تمرین دکمه برچسب و قرار دادن عکس و بستن فرم

import tkinter as tk
from tkinter import Tk,Button,Label,PhotoImage
frm=Tk(className='vira')
frm.title('به کلاس پایتون خوش آمدید')
frm.geometry('600x700')
frm.resizable(width=False,height=False)
frm.configure(bg='gold')


lbl=Label(frm,text="start",bg='lightblue',fg='black',font=50,).pack(side='bottom',fill='both',expand=True)
img=PhotoImage(file='play.png')
img2=PhotoImage(file='stop.png')
l=Label(frm,image=img).pack(side='bottom',fill='both',expand=True)
b1=Button(frm,text='click me',fg='red',bg='white',font=30,activebackground='black',image=img2)
b1.pack(side='left',expand=True)

b2=Button(frm,text='click me too',fg='red',bg='blue',font=30)
b2.pack(side='left',expand=True)

b3=Button(frm,text='The end',fg='red',bg='green',command=lambda :frm.destroy(),font=30)
b3.pack(side='left',expand=True)



frm.mainloop()
