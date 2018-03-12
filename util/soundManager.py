# Imports
from core.parameters import *
import pygame

class SoundManager:
    
    def __init__(self):
        try:
            if not(args.nodrawing):
                pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
                self.__effectLeft = pygame.mixer.Sound("resources/cheese_left.wav")
                self.__effectRight = pygame.mixer.Sound("resources/cheese_right.wav")
                self.__effectBoth = pygame.mixer.Sound("resources/cheese_both.wav")
                self.__nosound = False
            else:
                1/0 
        except:
            self.__effectLeft = ""
            self.__effectRight = ""
            self.__effectBoth = ""
            self.__nosound = True
    
    
    def playSound(self,effect):
        if self.__nosound or args.nodrawing:
            ()
        else:
            try:
                effect.play()
            except:
                ()
                    
    def playSoundLeft(self):
        self.playSound(self.__effectLeft)
        
    def playSoundRight(self):
        self.playSound(self.__effectRight)
           
    def playSoundBoth(self):
        self.playSound(self.__effectBoth)
    
