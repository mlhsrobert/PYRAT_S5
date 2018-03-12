from core.parameters import *
from queue import Queue
import queue
import multiprocessing as mp
import os
import signal
import random

from core.MazeInfo import *
from player.AI_Manager import *
from util.errors import *

class Player:
    
    def __init__(self, location, randomStart, mazeSize): 
        
        if type(mazeSize) != tuple:
            raise ArgsException("Player.__init__ : mazeSize is not a tuple")
        if type(mazeSize[0]) != int or type(mazeSize[1]) != int:
            raise ArgsException("Player.__init__ : mazeSize is not a tuple of int")  
        if mazeSize[0]<0 or mazeSize[1]<0 :
            raise ArgsException("Player.__init__ : mazeSize should not negative")               
        
        if type(location) != tuple:
            raise ArgsException("Player.__init__ : Location is not a tuple")
        if type(location[0]) != int or type(location[1]) != int:
            raise ArgsException("Player.__init__ : Location is not a tuple of int")
        if location[0]<0 or location[0]>=mazeSize[0] or location[1]<0 or location[1]>=mazeSize[1]:
            raise ArgsException("Player.__init__ : Location is not in the maze")
        
        if type(randomStart) != bool:
            raise ArgsException("Player.__init__ : randomStart is not a boolean")

        #Number of pieces of cheese eaten
        self._score = 0.
        # If >1 : how many turns to wait to play again
        self._stuckTurns = 0 
        # Number of moves
        self._moves = 0
        # Number of missed turns
        self._miss = 0
        # Number of turns in mud
        self._mud = 0 
        # Time used by the preprocessinf function
        self._prepDelay = 0.
        # Time used by the turn function
        self._turnDelay = 0.
        
        #If randomStart : info contains maze size
        #If not randomStart : info contains the player location
        if randomStart:
            a = random.randint(0, mazeSize[0]-1)
            b = random.randint(0, mazeSize[1]-1)
            self._location = (a,b)
        else:
            self._location = location
                        
        self._name = "no name"
 
    # Get Functions
    def plays(self):
        return 
        
    def getName(self):
        return self._name
        
    def getScore(self):
        return self._score
    
    def getMoves(self):
        return self._moves
    
    def getMissedTurns(self):
        return self._miss
    
    def getMudFence(self):
        return self._mud
    
    def getLocation(self):
        return self._location
                
    def getStuckTurns(self):
        return self._stuckTurns
    
    def gotPieceOfCheese(self):
        self._score += 1
        
    def gotHalfPieceOfCheese(self):
        self._score += 0.5
        
    def reduceStuckTurns(self):
        self._stuckTurns -= 1
        
    def isOnAPieceOfCheese(self, mazeInfo):
        return False
            
    def sendInfoForPreProcessing(self, otherPlayer_location, maze, pieces_of_cheese):
        return
    
    def sendInfoForATurn(self, otherPlayer_location, otherPlayer_Score, pieces_of_cheese):
        return    
    
    def sendInfoForPostProcessing(self, otherPlayer_location, otherPlayer_Score, pieces_of_cheese):
        return  
    
    def putHumanDecision(self, decision):
        return
    
    def sendEndingSignal(self):
        return
    
    def askForADecision(self, opponentLocation, opponentScore, piecesOfCheese):
        return
            
    def demandDecisionAndMove(self,synchronous,maze):
        return "None"  
        
    def computeDelays(self):
        return   
            
    def stopAIProcess(self):
        return    
        
    def getStatsInformation(self):
        return self._score, self._moves, self._miss, self._mud, self._prepDelay, self._turnDelay
    
    def getInitialDisplayInformation(self):
        return self._name , self._location 
    
    def getDisplayInformation(self):
        return (self._location, (self._score, self._moves, self._miss, self._mud))   