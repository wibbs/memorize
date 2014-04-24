from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
import random
import time

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
        self.buttonList = [self.button1, self.button2, self.button3, self.button4]

        #add buttons to the screen                                                                                                                                                                                                 
        for button in self.buttonList:
            self.add_widget(button)

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

    def on_touch_down(self, touch):
        self.buildChallenge()


    def buildChallenge(self):
        delay = 0
        lengthOfChallenge = self.round + 1
        choice = random.choice(self.buttonList)
        self.challenge.append(choice)

        #play the challenge to the player
        for x in self.challenge:
            delay += .5
            self.blinkSquare(x,delay)
            print x

class MemorizeApp(App):

    def build(self):
        game= MemorizeGame()
        return game

if __name__ == "__main__":
    MemorizeApp().run()