from player.Player import *
from player.AIPlayer import *
from player.HumanPlayer import *
from player.InactivePlayer import *

import pygame

class PlayerDisplay():
    
    def __init__(self, player):
        
        if type(player) == InactivePlayer:
            self.__isAlive = False
        else :
            self.__isAlive = True      
            
        self.__name, self.__location= player.getInitialDisplayInformation()
        self.__nextLocation = self.__location
        self.__score = 0
        self.__moves = 0
        self.__miss = 0
        self.__mud = 0
        
        self.__timeToGo = pygame.time.get_ticks()
        
        self.__staticImage = "empty"
        self.__portraitImage = "empty"
        self.__movingImage = "empty"
    
    def isAlive(self):
        return self.__isAlive
    
    def getScore(self):
        return self.__score    
    
    def getScoreStr(self):
        return "Score: "+str(self.__score)
    
    def getName(self):
        return self.__name
    
    def getMoves(self):
        return self.__moves
    
    def getMovesStr(self):
        return "Moves : "+str(self.__moves)    
    
    def getMiss(self):
        return self.__miss
    
    def getMissStr(self):
        return "Miss : "+str(self.__miss)    
    
    def getMud(self):
        return self.__mud
    
    def getMudStr(self):
        return "Mud : "+str(self.__mud) 
    
    def getLocation(self):
        return self.__location
    
    def getNextLocation(self):
        return self.__nextLocation
    
    def setTimeToGo(self, time):
        self.__timeToGo = time
        
    def setNextLocation(self, location):
        self.__nextLocation = location
        
    def updateLocation(self):
        self.__location = self.__nextLocation
    
    def updateGameInfo(self, info):
        self.__score, self.__moves, self.__miss, self.__mud = info
        
    def initStaticImage(self, file, scale):
        self.__staticImage = pygame.transform.smoothscale(pygame.image.load(file),scale)
        if not(self.__isAlive):
            self.__staticImage = self.__staticImage.convert()
            self.__staticImage.set_alpha(0)        
        
    def initPortraitImage(self, file, scale):
        self.__portraitImage = pygame.transform.smoothscale(pygame.image.load(file),scale)
        
    def initMovingImage(self, file, scale):
        self.__movingImage = pygame.transform.smoothscale(pygame.image.load(file),scale)
        if not(self.__isAlive):
            self.__movingImage = self.__movingImage.convert()
            self.__movingImage.set_alpha(0)        
        
    def getStaticImage(self):
        return self.__staticImage
    
    def getMovingImage(self):
        return self.__movingImage
    
    def getPortraitImage(self):
        return self.__portraitImage
    
    def processMoveAnimation(self, maze, turnTime):
        if self.__timeToGo <= pygame.time.get_ticks() or self.__location == self.__nextLocation:
            self.__location = self.__nextLocation
            drawLocation = self.__location
            image = self.__staticImage
        else:
            prop = (self.__timeToGo - pygame.time.get_ticks()) / (maze[self.__location][self.__nextLocation] * turnTime)
            i, j = self.__location
            ii, jj = self.__nextLocation
            drawLocation = i * prop + ii * (1 - prop), j * prop + jj * (1 - prop)
            if ii > i:
                image = pygame.transform.rotate(self.__movingImage, 270)
            elif ii < i:
                image = pygame.transform.rotate(self.__movingImage, 90)
            elif j < jj:
                image = pygame.transform.rotate(self.__movingImage, 0)
            else:
                image = pygame.transform.rotate(self.__movingImage, 180)        
                
        return drawLocation, image
    