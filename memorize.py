from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.vector import Vector
import random
import time
import sys

from kivy.clock import Clock

class MemorizeGame(GridLayout):
    def __init__(self, **kwargs):
        super(MemorizeGame, self).__init__(**kwargs)
        self.challenge = []
        self.round = 1
        self.cols = 2

        #create buttons                                                                                                                                                                                                            
        self.button1 = Button(text='', background_color=(0,0,1,1))
        self.button2 = Button(text='', background_color=(0,1,1,1))
        self.button3 = Button(text='', background_color=(1,0,1,1))
        self.button4 = Button(text='', background_color=(0,1,0,1))
        self.startBtn = Button(text='Start Round')
        self.quitBtn = Button(text="Quit")
        self.buttonList = [self.button1, self.button2, self.button3, self.button4]

        self.startBtn.bind(on_press=self.buildChallenge)
        self.quitBtn.bind(on_press=self.quit)

        #add buttons to the screen                                                                                                                                                                                                 
        for button in self.buttonList:
            self.add_widget(button)
            button.bind(on_press=self.getClickedButton)
        self.add_widget(self.startBtn)
        self.add_widget(self.quitBtn)


    def blinkSquare(self, targetButton, delay):
        '''
        changes the squares color to 1,1,1,1 then changes it back after .3 seconds.
        delay tells the clock how long ot wait before blinking the next square
        see buildChallenge() for delay usage
        '''
        originalColor = targetButton.background_color
        def set_color(*args):
            targetButton.background_color = (1, 1, 1, 1)
        def reset_color(*args):
            targetButton.background_color = (originalColor)

        Clock.schedule_once(set_color, delay)
        delay += .3
        Clock.schedule_once(reset_color, delay)

    '''
    def on_touch_down(self, touch):
        print touch
    '''

    def getClickedButton(self, instance):
        #check to see if what the user pressed is the right button
        self.userSelected = instance
        print instance

    def buildChallenge(self, instance):
        delay = 0
        lengthOfChallenge = self.round + 1
        choice = random.choice(self.buttonList)
        self.challenge.append(choice)

        #play the challenge to the player
        print "round:", self.round
        for x in self.challenge:
            delay += .5
            self.blinkSquare(x,delay)
            print x


    def quit(self, instance):
        sys.exit()
    #def userAttempt():


class MemorizeApp(App):

    def build(self):
        self.title = "Memorize"
        #parent = Widget()
        game = MemorizeGame()
        #startbtn = Button(text='start')
        #game.add_widget(startbtn)
        return game

if __name__ == "__main__":
    MemorizeApp().run()