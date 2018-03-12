from core.parameters import *
from queue import Queue
import queue
import multiprocessing as mp
import os
import signal
import random

from core.MazeInfo import *
from player.Player import *

class HumanPlayer(Player):
    
    def __init__(self, location, randomStart, mazeSize):
        
        Player.__init__(self,location, randomStart, mazeSize) 
        #This queue is used to communicate with the display to know when a key is pressed
        self._qFromDisplay = mp.Queue()
                  
        self._name = str("human")
 
    # An HumanPlayer plays (it is active)
    def plays(self):
        return True   
    
    # The player can move if it is not in mud                            
    def canMove(self):
        return self._stuckTurns <= 0
    
    # Check if the player is on a piece of cheese        
    def isOnAPieceOfCheese(self, mazeInfo):
        if self.canMove():
            return self._location in mazeInfo.getPiecesOfCheese()    
        else:
            return False
        
    # Convert the decision taken by an AI into a new location
    def cellOfDecision(self, decision):
        
        a, b = self._location
        if decision == "U":
            return (a,b+1)
        elif decision == "D":
            return (a,b-1)
        elif decision == "L":
            return (a-1,b)
        elif decision == "R":
            return (a+1,b)
        elif decision == "None":
            return (a,b)
        else:
            raise ArgsException("Player.cellOfDecision : incorrect decision. Received : "+str(decision) + " (" + str(type(decision)) + ")")
        
        
    # This function moves a player according to its decision
    # when the player passes throw mud, it moves then it is stuck
    def move(self, decision, maze):
        if self.canMove():
            cell = self.cellOfDecision(decision)
            if cell in maze[self._location]:
                self._stuckTurns = maze[self._location][cell]
                self._location = cell
                self._moves += 1
            else :
                self._miss += 1 
        else:
            self._mud += 1
              
    def getDecision(self, synchronous):
        return str(self._qFromDisplay.get(synchronous))
    
    # Demand the player to give right now its decision and to move according to it       
    def demandDecisionAndMove(self,synchronous,maze):
        try:
            decision = self.getDecision(synchronous)
        except:
            decision = "None"
            
        self.move(decision, maze)
        return decision                    
    
    # Called by the display to transfer a decision from the keyboard
    def putHumanDecision(self,decision):    
        while not self._qFromDisplay.empty():
            self._qFromDisplay.get()
        self._qFromDisplay.put(decision)            