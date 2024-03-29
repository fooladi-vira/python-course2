## تمرین ایجاد موزیک پلیر

import pygame,tkinter
from tkinter import  StringVar, Tk,Label,Button,messagebox,Listbox,PhotoImage
from tkinter.filedialog import askdirectory
import os



music_player=Tk()
music_player.title("my music player")
music_player.geometry("800x800")
music_player.configure(bg='aqua')
directroy= askdirectory()
os.chdir(directroy)
song_list=os.listdir()

play_list=Listbox(music_player,font="Helvetica 12 bold",bg='yellow')
for item in song_list:
    pos =0
    play_list.insert(pos,item)
    pos += 1
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load((play_list.get(tkinter.ACTIVE)))
    var.set(play_list.get(tkinter.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

def showmsg():
    lblmsg=Label(music_player,text=' به اپلیکیشن ویرا خوش آمدید',bg='orange',fg='black',font=('B mitra',30),)
    lblmsg.grid()

def showpic():
    mypic=PhotoImage(file='1.png')
    lblpic=Label(music_player,image=mypic)
    lblpic.image=mypic
    lblpic.grid()

def destroy_form():
    if messagebox.askyesnocancel('خروج','آیا میخواهید خارج شوید'):
        music_player.destroy()





Button1 = Button(music_player,width=5,height=3,font="Helvetica 12 bold",text="PLAY",command=play,bg="blue",fg="white")
Button2 = Button(music_player,width=5,height=3,font="Helvetica 12 bold",text="STOP",command=stop,bg="red",fg="white")                
Button3 = Button(music_player,width=5,height=3,font="Helvetica 12 bold",text="PAUSE",command=pause,bg="purple",fg="white")
Button4 = Button(music_player,width=5,height=3,font="Helvetica 12 bold",text="UNPAUSE",command=unpause,bg="orange",fg="white")

var = StringVar()
song_title =Label(music_player,width=10,height=3,font="Helvetica 12 bold",textvariable=var)

song_title.grid()
Button1.grid()
Button2.grid()
Button3.grid()
Button4.grid()
play_list.grid()



btnMsg=Button(music_player,text='نمایش پیام',fg='red',bg='aqua',font=('B mitra',30),activebackground='black',command=showmsg)
btnMsg.grid()


btnMsg=Button(music_player,text='نمایش عکس',command=showpic,bg='lightblue',fg='black',font=('B mitra',30))
btnMsg.grid()

exit_btn= Button(music_player, text='exit', fg='black', bg='red',command=destroy_form,font=('B mitra',30))
exit_btn.grid()

music_player.mainloop()


