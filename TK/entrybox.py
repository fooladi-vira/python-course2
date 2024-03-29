from tkinter import *

root = Tk()
root.geometry(("500x500+100+100"))
root.configure(bg="#FFFF00")
L1 = Label(root, text = "User Name")

L1.pack( side = LEFT)


#Create a Label
img=PhotoImage(file='1.png')
Label(root, text= "Text",image=img, font= ('Helvetica 18'), bg= '#ab23ff').pack(ipadx= 50, ipady=50, padx= 20)

# ایجاد ویجت لیبل
label = Label(root, text='Hello World!')

# تنظیم پس‌زمینه شفاف برای ویجت
label.configure(bg= '#ab23ff')
label.place(x=100, y=100)
E1 = Entry(root, bd = 5)
E1.pack(side = RIGHT)
root.mainloop()