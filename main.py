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

class userInput(GridLayout,Widget):
    cardName = ObjectProperty(None)
    cardDesc = ObjectProperty(None)
    pass

class offlineScreen(Screen):
    def __init__(self,**kwargs):
        self.cam = camera()
        self.ui = userInput()
        self.popupUi = Popup(title="User Query", content=self.ui, size_hint=(None, None), size=(400, 400))
        self.popupCamera = Popup(title="Camera", content=self.cam, size_hint=(None, None), size=(400, 400))
        super(Screen,self).__init__(**kwargs)

    def cameraPop(self):
        self.popupCamera.open()


    def userInp(self):

        self.popupUi.open()

    def offRun(self):
        pass



class onlineScreen(Screen):


    def show_popup(self):
        show = camera()

        self.popupWindow = Popup(title="Camera", content=show, size_hint=(None, None), size=(400, 400))
        self.popupWindow.open()

    def userInp(self):
        show = userInput()

        self.popupWindow = Popup(title="User Query", content=show, size_hint=(None, None), size=(400, 400))
        self.popupWindow.open()


    #ML Code for online

    def onlRun(self):
        pass







#Kivy App Builder

kv = Builder.load_file("main_style.kv")

class theApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    theApp().run()










