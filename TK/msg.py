

from tkinter import messagebox,Button, Tk

def helloCallBack(txt):
   msg = messagebox.showinfo( "Hello ", "سلام "+'  '+txt)

def destroy_form():
   top.destroy()



top = Tk()
top.geometry("600x700")
top.configure(bg='light blue')
top.title(" نمایش پیام")


B = Button(top, text = "سفارش کالا", bg='pink' ,fg='blue',font=('B mitra',50),command =lambda : helloCallBack('Vira'))
B.pack()


btnExit=Button(top,text='خروج', bg='pink' ,fg='blue',font=('B mitra',50),command=destroy_form)
btnExit.pack()

top.mainloop()