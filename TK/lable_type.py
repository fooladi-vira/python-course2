
from tkinter import *
import tkinterwidgets as tkw 

root=Tk()
root.config(bg='yellow')

root.geometry("500x500+100+100")
label=Label(root,text='Default Label')
label.pack()

trans_label=tkw.Label(root,text='tkinterwidgets Label',opacity=0.7)
trans_label.pack(pady=10)

image1 = PhotoImage(file='1.png')
panel1 = Label(root, image=image1)
panel1.pack(side='left', fill='both', expand='yes')
label1 = Label(panel1, text='here i am',font=30)
label1.pack(side='left')
button2 = Button(panel1, text='button2')
button2.pack(side='left')


Label(root, text="Flat border", borderwidth=3, relief="flat", padx=5, pady=10).pack(padx=5, pady=10)
Label(root, text="raised border", borderwidth=3, relief="raised", padx=5, pady=10).pack(padx=5, pady=10)
Label(root, text="sunken border", borderwidth=3, relief="sunken", padx=5, pady=10).pack(padx=5, pady=10)
Label(root, text="ridge border", borderwidth=3, relief="ridge", padx=5, pady=10).pack(padx=5, pady=10)
Label(root, text="solid border", borderwidth=3, relief="solid", padx=5, pady=10).pack(padx=5, pady=10)
Label(root, text="groove border", borderwidth=3, relief="groove",padx=5, pady=10).pack(padx=5, pady=10)

root.mainloop()

