
# تمرین چگ باکس

from tkinter import *


root = Tk()
root.geometry('500x600')
root.resizable(width=False,height=False)
root.configure(bg='gold')

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()



def bg_change():
    print(CheckVar1.get(),CheckVar2.get(),CheckVar3.get())
    if CheckVar1.get()==1:
        root.configure(bg='blue')
    elif CheckVar2.get()==1:
        root.configure(bg='green')
    elif CheckVar3.get()==1:
        root.configure(bg='aqua')
    else:
        root.configure(bg='gold')



lblpic=Label(root,text="تغییر رنگ پس زمینه",font=30)
lblpic.pack(side='top')
check_button1 = Checkbutton(root, text = "آبی",font=30, variable = CheckVar1, command=bg_change )
check_button2 = Checkbutton(root, text = "سبز",font=30, variable = CheckVar2, command=bg_change)
check_button3 = Checkbutton(root, text="سبزآبی",font=30, variable=CheckVar3, command=bg_change)
check_button3.pack(side='top')
check_button2.pack(side='top')
check_button1.pack(side='top')
# نمایش پنجره



def select():
    selected_items = listbox.curselection()
    for i in selected_items[::-1]:
        print(listbox.get(i))
        
listbox = Listbox(root,)

listbox.insert(1, 'laptop')
listbox.insert(2, 'case')
listbox.insert(3, 'mouse')
listbox.pack()



btn_select=Button(root,text='select',bg='blue',activebackground='red',command=select)
btn_select.pack(side='bottom')










root.mainloop()

