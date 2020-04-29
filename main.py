# imports for kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import json
from threading import Thread
import time 
# imports for ML Software here

import pandas as pd
# Given that descriptions are series of ordered words, we can convert those series into numerical feature vectors
from sklearn.feature_extraction.text import CountVectorizer
# Reduce the weightage of certain words like (the, is, a, an, etc)
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
import pickle
from kivy.config import Config

Config.set('graphics','resizable',True)



#end of imports
#Ml Class and organization

class model():
    def __init__(self):
        self.modelList =[]  #contains models in this order [type,power,toughness,mana-cost,color]
        filelist=['type_model.obj','power_model.obj','tough_model.obj','mana_model.obj','color_model.obj']
        for x in filelist:
            with open(x,'rb') as f:
                self.modelList.append(pickle.load(f))
    def prediction(self,X):
        outputList = []
       # print(self.modelList)
        for piece in self.modelList:

            outputList.append(piece.predict([X])[0])
        return outputList



class loadPop(FloatLayout):
    pass


class WindowManager(ScreenManager):
    pass


    man = ObjectProperty(None)

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
        offSubmit = ObjectProperty(None)
        self.popupUi = Popup(title="User Query", content=self.ui, size_hint=(None, None), size=(400, 400))
        self.popupCamera = Popup(title="Camera", content=self.cam, size_hint=(None, None), size=(400, 400))
        self.ml= model()
        self.solution = []
        super(Screen,self).__init__(**kwargs)

    def cameraPop(self):
        self.popupCamera.open()


    def userInp(self):

        self.popupUi.open()

    def offRun(self):
        self.modifier = typeManager()
        loader = loadPop()
        loadingScreen = Popup(title="Modeling",content=loader,size_hint=(None,None),size=(400,400))
        loadingScreen.open()


        #self.threader = Thread(self.ml.prediction,self.ui.cardDesc.text)
        #solution = self.threader.join()
        print(self.ui.cardDesc.text)
        solution = self.ml.prediction(self.ui.cardDesc.text)

        print(solution)

        loadingScreen.dismiss()
        self.offSubmit.text="View Output"

        manaCost = 0
        for x in solution[3]:
            if(x != "{" and x !="}"):
                manaCost=manaCost+1

        solution.append(manaCost)
        self.solution = solution


        cardDets = {
            "cards":{
            "artist":"Grizzly",
            "borderColor":"black",
            "colorIdentity":solution[-1],
            "colorIndicator":solution[-1],   #to be changed
            "colors":solution[-1],
            "convertedManaCost":manaCost,
            "faceConvertedManaCost":manaCost,
            "flavorText":self.ui.cardDesc.text},
            "foreignData":"English",
            "frameEffects":{"draft"},
            "frameVersion":"future",
            "isMtgo":"false",
            "life":solution[2],
            "manaCost":solution[-2],
            "mcmId":"314312",
            "mcmMetaId":"468313",
            "name":self.ui.cardName.text,
            "number":"042",
            "originalText":self.ui.cardDesc.text,
            "originalType":solution[0],
            "power":solution[1],
            "rarity":"basic"

        }

    def untiRun(self):
        self.modifier.generate()






class cardScreen(Screen):
    def __init__(self,**kwargs):
        super(Screen,self).__init__(**kwargs)
        descLabel = ObjectProperty(None)
        nameLabel = ObjectProperty(None)
        typeLabel = ObjectProperty(None)



class typeManager():

    def __init__(self):
        self.offScreen = App.get_running_app().root.get_screen("offline")


    def generate(self):
        self.resScreen = App.get_running_app().root.get_screen("card")

        self.resScreen.descLabel.text = self.offScreen.ui.cardDesc.text
        self.resScreen.nameLabel.text = self.offScreen.ui.cardName.text
        self.resScreen.typeLabel.text = self.offScreen.solution[0]
























#non functional ( needs runway implementation)

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










