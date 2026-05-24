from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Running...")

if __name__ == "__main__":
    MyApp().run()