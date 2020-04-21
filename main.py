# imports for kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

# imports for ML Software





#end of imports


class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):
    pass




class offlineScreen(Screen):
    pass


class onlineScreen(Screen):
    pass
















#Kivy App Builder

kv = Builder.load_file("main_style.kv")

class theApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    theApp().run()










