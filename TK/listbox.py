from tkinter import *


def select_l():
    selected_items = listbox.curselection()
    for i in selected_items[::-1]:
        print(listbox.get(i))

root = Tk()
root.geometry('300x300')

listbox = Listbox(root,)

listbox.insert(1, 'laptop')
listbox.insert(2, 'case')
listbox.insert(3, 'mouse')


btn_select=Button(root,text='select',bg='blue',activebackground='red',command=select_l)
btn_select.pack(side='bottom')
btn_select.flash()

listbox.pack()


button = Button(root, text="بستن", command=root.destroy)
button.pack(side="bottom")

root.mainloop()









# مرتبط کردن رویداد کلیک بر روی آیتم با تابع on_select
#listbox.bind("<<ListboxSelect>>", on_select)


# def on_select(event):
#     # دریافت محتوای آیتم انتخاب شده و چاپ آن در کنسول
#     selected_item = event.widget.get(event.widget.curselection())
#     print(selected_item)