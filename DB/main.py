from cProfile import label
from tkinter import Entry, Tk,Label,Button,LEFT

def insert_record():
    label.config(text="record")

def read_record():
    label.config(text="read")

def close():
    main_window.destroy()

main_window=Tk()
main_window.geometry('800x800')
label_name=Label(main_window,text='label_name',pady=10)
label_BC_No=Label(main_window,text='label_BC_No',pady=10)
label_performa=Label(main_window,text='label_performa',pady=10)
label_arz=Label(main_window,text='label_arz',pady=10)





#input

name_input=Entry(main_window,bg='#abbfff')
BC_No_input=Entry(main_window,bg='#abbfff')
performa_input=Entry(main_window,bg='#abbfff')
arz_input=Entry(main_window,bg='#abbfff')



label_name.grid(row=1  , column=2)
name_input.grid(row=1  , column=3)
label_BC_No.grid(row=2  , column=2)
BC_No_input.grid(row=2  , column=3)
label_performa.grid(row= 3 , column=2)
performa_input.grid(row= 3 , column=3)
label_arz.grid(row= 4 , column=2)
arz_input.grid(row= 4 , column=3)




record_btn=Button(main_window,text=" insert record",command=read_record,bg="#000f00",fg='white')
record_btn.grid(row=6,column=3)
read_btn=Button(main_window,text=" read",command=read_record,bg="#00f000",fg='white')
read_btn.grid(row=7,column=3,columnspan=1)



#record_btn.pack(side=LEFT)
main_window.mainloop()