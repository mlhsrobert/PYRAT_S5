from display.Display import *
from core.parameters import *
from queue import Queue
import queue
from threading import Thread
from player.Player import *
import pygame

class DisplayController():
    
    def __init__(self, screen, infoObject, mazeInfo, ratPlayer, pythonPlayer):
        
        self.__ratName = ratPlayer.getName()
        self.__pythonName = pythonPlayer.getName()
        
        # Queues used for the communication with the display
        self.__q1DrawingInfo = Queue() #q
        self.__q2QuitFromDisplay = Queue() #q_render_in
        self.__q3QuitFromCore = Queue() #q_quit
        self.__q4Text = Queue() #q_info
        
        #Store if the display asks to quit
        self.__stopFromDisplay = False
        
        # If there is drawing, the the display is launched in a thread
        if not(args.nodrawing):
            self.__display = Display(screen, mazeInfo)
            self.__draw = Thread(target=self.__display.run, args=(self.__q1DrawingInfo, self.__q2QuitFromDisplay, 
                                                                  self.__q3QuitFromCore, self.__q4Text, 
                                                                  ratPlayer, pythonPlayer, infoObject))              
            self.__draw.start() 
            
    def getStopFromDisplay(self):
        return self.__stopFromDisplay
    
    def sendEndGameMessage(self, code):
        text =""
        if code == "both" :
            text = "The Rat(" + self.__ratName + ") and the Python (" + self.__pythonName + ") got the same number of pieces of cheese!"
        elif code == "rat" :
            text = "The Rat (" + self.__ratName + ") won the match!"
        elif code == "python":
            text = "The Python (" + self.__pythonName + ") won the match!"
        elif code == "ratOnly" :
            text = "The Rat (" + self.__ratName + ") got all pieces of cheese!"
        elif code == "pythonOnly":
            text = "The Python (" + self.__pythonName + ") got all pieces of cheese!"
        elif code == "cheese" :
            text = "No more pieces of cheese!"
        elif code == "turns":
            text = "max number of turns reached!"
        self.sendText(text)
        
            
    def sendText(self, text):
        if not(args.nodrawing):
            self.__q4Text.put(text)
        else:
            print(text, file=sys.stderr)
        
    def sendDrawingInfo(self, piecesOfCheese, ratInfo, pythonInfo):
        self.__q1DrawingInfo.put((piecesOfCheese, ratInfo, pythonInfo))
        
    def haveToExit(self):
        try:
            self.__q2QuitFromDisplay.get(False)
            return True
        except queue.Empty:
            return False
        
    def stopFromDisplay(self):
        try:
            self.__q2QuitFromDisplay.get(False)
            self.__stopFromDisplay = True
            return True
        except queue.Empty:
            return False    
        
    
    def stopGraphicalInterface(self):       
        if not(args.nodrawing):
            if args.auto_exit:
                self.__q3QuitFromCore.put("")
            else:
                if not self.__stopFromDisplay:
                    while 1:
                        pygame.event.pump()  
                        if self.haveToExit():
                            self.__q3QuitFromCore.put("")
                            break
            if self.__draw.is_alive():
                self.__q2QuitFromDisplay.get()    