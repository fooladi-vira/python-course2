import DB
from tkinter import Tk,Button,Label,PhotoImage,Frame,Entry,messagebox,Listbox

name_DB='vira.db'
sql_create_table='''CREATE TABLE IF NOT EXISTS user
                (code INTEGER PRIMARY KEY ,
                name TEXT, last_name TEXT,id_course INTEGER, course TEXT,phone TEXT,price INTEGER,pay TEXT)'''
DB=DB.DB_Vira(name_DB,sql_create_table)

def register():
    name=name_box.get()
    last_name=family_box.get()
    code=int(code_box.get())
    phone=phone_box.get()
    ID_course=int(course_box_id.get())
    name_course=course_box.get()
    price_course=int(course_price_box.get())
    pay=pay_box.get()
    DB.add_user(name,last_name,code,phone,ID_course,name_course,price_course,pay)
    messagebox.showinfo('ثبت کار آموز',"کاربر ثبت شد")

def edit_user():
    name=name_box.get()
    last_name=family_box.get()
    code=int(code_box.get())
    phone=phone_box.get()
    ID_course=int(course_box_id.get())
    name_course=course_box.get()
    price_course=int(course_price_box.get())
    pay=pay_box.get()
    DB.edit_user(name,last_name,code,phone,ID_course,name_course,price_course,pay)
    messagebox.showinfo('ویرایش کار آموز',"کاربر ویرایش شد")

def del_user():
    code=int(code_box.get())
    DB.delete_user(code)
    messagebox.showinfo('حذف کار آموز',"کاربر حذف شد")


def print_user():
    rows=DB.select_users()
    pos=0
    page2=Tk()
    page2.title(' کارآموزان آموزشگاه کامپیوتر ویرا')
    page2.geometry('400x400+600+200')
    page2.resizable(width=False,height=False)
    list_box = Listbox(page2, width=100, font=("Times new roman",15), bg="#33FFF3",  cursor="hand2", bd=2, )
    list_box.pack(side='right')
    for r in rows:
            list_box.insert(pos, r)
            pos=+1

if __name__=='__main__':
    main_window=Tk(className='vira')
    main_window.title('آموزشگاه کامپیوتر ویرا')
    main_window.geometry('500x500+400+200')
    main_window.resizable(width=False,height=False)

    frame_logo = Frame(main_window)
    frame_logo.pack(side='top')
    frame_empty = Frame(main_window,height=50)
    frame_empty.pack(side='top')
    frame2 = Frame(main_window)
    frame2.pack(side='top')
    frame3 = Frame(main_window)
    frame3.pack(side='top')
    frame1 = Frame(main_window)
    frame1.pack(side='top')
    frame_empty = Frame(main_window,height=50)
    frame_empty.pack(side='top')
    frame_price = Frame(main_window)
    frame_price.pack(side='top')
    frame4 = Frame(main_window)
    frame4.pack(side='bottom')

    mypic=PhotoImage(file='logo.png')
    lblpic=Label(frame_logo,bg='khaki',image=mypic,width=100,height=100,justify='right',)
    lblpic.image=mypic
    lblpic.pack(side='right')
    Label(frame_logo,text='فرم ثبت نام کارآموز',bg='khaki',font=('B nazanin',25),width=60,height=2).pack(side='right')

    lbl_name_box=Label(frame2,text='نام ',width=8,font=('B nazanin',12)).pack(side='right')
    name_box = Entry(frame2,width=12,font=20,bd=5,)
    name_box.pack( side ='right')
    lbl_family_box=Label(frame2,text=' نام خانوادگی ',width=9,font=('B nazanin',12)).pack(side='right')
    family_box = Entry(frame2,width=15,font=20,bd=5,)
    family_box.pack( side ='right')

    lbl_code_box=Label(frame3,text='کد ملی',width=8,font=('B nazanin',12)).pack(side='right')
    code_box = Entry(frame3,width=12,font=20,bd=5,)
    code_box.pack( side ='right')
    lbl_phone_box=Label(frame3,text='تلفن',width=9,justify='right',font=('B nazanin',12)).pack(side='right')
    phone_box = Entry(frame3,width=15,font=20,bd=5,)
    phone_box.pack( side ='right')


    lbl_course_box_id=Label(frame1,text='کد دوره',width=8,font=('B nazanin',12)).pack(side='right')
    course_box_id = Entry(frame1,width=12,font=20,bd=5,)
    course_box_id.pack( side ='right')
    lbl_course_box=Label(frame1,text='دوره',width=9,padx=2,font=('B nazanin',12)).pack(side='right')
    course_box = Entry(frame1,width=15,font=20,bd=5,)
    course_box.pack( side ='right')

    lbl_course_price_box=Label(frame_price,text='هزینه دوره',width=8,font=('B nazanin',12)).pack(side='right')
    course_price_box = Entry(frame_price,width=12,font=20,bd=5,)
    course_price_box.pack( side ='right')
    lbl_pay_box=Label(frame_price,text='پرداخت',width=9,padx=2,font=('B nazanin',12)).pack(side='right')
    pay_box = Entry(frame_price,width=15,font=20,bd=5,)
    pay_box.pack( side ='right')

    button_reg = Button(frame4,text='ثبت نام',font=('B nazanin',14),width=8,height=2,bd=5,padx=10,pady=10,bg='pink',command= register)
    button_reg.pack( side ='right')

    button_edit = Button(frame4,text='ویرایش',font=('B nazanin',14),width=8,height=2,bd=5,padx=10,pady=10,bg='light green',command= edit_user)
    button_edit.pack( side ='right')

    button_del = Button(frame4,text='حذف',font=('B nazanin',14),width=8,height=2,bd=5,padx=10,pady=10,bg='violet',command= del_user)
    button_del.pack( side ='right')

    button_print = Button(frame4,text='چاپ',font=('B nazanin',14),width=8,height=2,bd=5,padx=10,pady=10,bg='light blue',command= print_user)
    button_print.pack( side ='right')

    main_window.mainloop()