from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="Olá Mundo! Esse é meu primeiro programa em kivy \n Sou SESIANO de veia, amo Jesus")
    
if __name__ == '__main__':
    MyApp().run()