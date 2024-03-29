from cgitb import text
from datetime import datetime
from email.mime import image
from tkinter.font import BOLD
from turtle import color, pos
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class AgeCalculator(App):
    def build(self):
        self.window=GridLayout()
        self.window.cols=1
        self.window.add_widget(Image(source=('1.png')))
        self.ageRequest=Label(text='enter your age',font_size='60sp', color='fffaaa',bold=True)
        self.window.add_widget(self.ageRequest)
        self.date=TextInput(
            multiline=False,
            padding_y=(30,30),
            padding_x=(30,30),
            size_hint=(1,0.7 ),
            font_size=30
        )
        self.window.add_widget(self.date)
        self.button=Button(
            text='calculate age',
            background_color="#ff00eeaa",
            color="#fff000",
            size=(40,40),
            pos=(300,250),
            size_hint=(0.5,0.7 ),
            font_size=30
        )
        self.button.bind(on_press=self.getAge)
        self.window.add_widget(self.button)

        return self.window
    def getAge(self,event):
        today=datetime.today().year
        print(today)
        dob=self.date.text
        age=int(today)- int(dob)
        self.ageRequest.text="you are "+str(int(age))+ "  years old"
ageCalculator=AgeCalculator()
ageCalculator.run()
