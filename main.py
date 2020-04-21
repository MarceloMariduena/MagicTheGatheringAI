# imports for kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

# imports for ML Software here








#end of imports


class WindowManager(ScreenManager):
    pass


class MainWindow(Screen,FloatLayout):
    pass

class camera(FloatLayout):
    pass

class userInput(GridLayout):
    pass

class offlineScreen(Screen):
    def cameraPop(self):
        self.show_popup()

    def show_popup(self):
        show = camera()

        self.popupWindow = Popup(title="Camera", content=show, size_hint=(None, None), size=(400, 400))
        self.popupWindow.open()

    def userInp(self):
        show = userInput()

        self.popupWindow = Popup(title="User Query", content=show, size_hint=(None, None), size=(400, 400))
        self.popupWindow.open()

    #def Pushed(self):
     #   self.popupWindow.dismiss()



class onlineScreen(Screen):
    def cameraPop(self):
        self.show_popup()

    def show_popup(self):
        show = camera()

        self.popupWindow = Popup(title="Camera", content=show, size_hint=(None, None), size=(400, 400))
        self.popupWindow.open()

    def userInp(self):
        show = userInput()

        self.popupWindow = Popup(title="User Query", content=show, size_hint=(None, None), size=(400, 400))
        self.popupWindow.open()


#Kivy App Builder

kv = Builder.load_file("main_style.kv")

class theApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    theApp().run()










