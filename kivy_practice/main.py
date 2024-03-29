from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def print_hello(self):
        print("HELLO")
    def build(self):
        lbl= Label(text='[color=1a2289b6][size=50][b]Vira[/b][/size][/color] APP',font_size=36,color='green',markup=True)
        lbl2= Label(text='enter your name',font_size=20,color='yellow')
        lbl3= Label(text='enter your family',font_size=20,color='blue')
        lbl4= Label(text='enter your [size=50][b]Age[/b][/size]',font_size='20sp',color='red',markup=True)
        txt=TextInput(multiline=False)
        self.txt=txt
        button = Button(text = "[size=20][b]send[/b][/size]",markup=True,background_color=(1,0,1,1),color=(0,1,0,1),size_hint=(0.5,.07 ),pos_hint={'x':.2 , 'y':.3 })
        button.bind(on_press=self.press)

        button_logo = Button(text = "[size=20][b]VIRA[/b][/size]",markup=True,background_color=(1,0,1,1),color=(0,1,0,1),size_hint=(0.4,.5 ),pos_hint={'x':.5 , 'y':.9 },background_normal='2.png')
        # markup text with different colour
        l2 = Label(text ="[ref=aaa][color=ff2289b6][b]Label [/color][/b][/ref] is Added\n[color=ff2289b6]Screen !!:):):):)[/color]",font_size ='20sp', markup = True)

       


        box=BoxLayout(orientation='vertical')
        box.add_widget(button_logo)
        box.add_widget(l2)
        box.add_widget(lbl)
        # box.add_widget(lbl2)
        
        # box.add_widget(lbl3)
        # box.add_widget(lbl4)
        box.add_widget(txt)
        box.add_widget(button)
        
        return box
    def press(self,event):
        self.txt.text="Hello guys send your Data"




if __name__ == "__main__":
    app = MainApp()
    app.run()