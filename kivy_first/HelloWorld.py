from turtle import color
import kivy
from kivy.app import App
from kivy.uix.label import Label
class Test(App):
    def build(self):
        return Label(text='HelloWorld',font_size='60sp',color='green')
# if __name__== "__main__":
#     Test.run()
lbl=Test()
lbl.run()