from core.parameters import *
from queue import Queue
import queue
import multiprocessing as mp
import os
import signal
import random

from core.MazeInfo import *
from player.AI_Manager import *
from player.Player import *
from util.errors import *

class AIPlayer(Player):
    
    def __init__(self, animal, file, location, randomStart, mazeSize, preparationTime, turnTime): 
        
        if type(animal) != str:
            raise ArgsException("AIPlayer.__init__ : animal is not a string") 
        
        if type(file) != str:
            raise ArgsException("AIPlayer.__init__ : file is not a string")         
        
        if type(mazeSize) != tuple:
            raise ArgsException("AIPlayer.__init__ : mazeSize is not a tuple")
        if type(mazeSize[0]) != int or type(mazeSize[1]) != int:
            raise ArgsException("AIPlayer.__init__ : mazeSize is not a tuple of int")  
        if mazeSize[0]<0 or mazeSize[1]<0 :
            raise ArgsException("AIPlayer.__init__ : mazeSize should not negative")               
        
        if type(location) != tuple:
            raise ArgsException("AIPlayer.__init__ : Location is not a tuple")
        if type(location[0]) != int or type(location[1]) != int:
            raise ArgsException("AIPlayer.__init__ : Location is not a tuple of int")
        if location[0]<0 or location[0]>=mazeSize[0] or location[1]<0 or location[1]>=mazeSize[1]:
            raise ArgsException("AIPlayer.__init__ : Location is not in the maze")
        
        if type(randomStart) != bool:
            raise ArgsException("AIPlayer.__init__ : randomStart is not a boolean")
        
        if type(preparationTime) != int:
            raise ArgsException("AIPlayer.__init__ : preparationTime is not a int")  
        if preparationTime < 0:
            raise ArgsException("AIPlayer.__init__ : preparationTime is negative") 
        
        if type(turnTime) != int:
            raise ArgsException("AIPlayer.__init__ : turnTime is not a int")  
        if turnTime < 0:
            raise ArgsException("AIPlayer.__init__ : turnTime is negative")            
        
                
        Player.__init__(self,location, randomStart, mazeSize)        
        
        self._q1ToAI = mp.Queue()
        self._q2FromAI = mp.Queue()

        self._process = mp.Process(target=AIManager.run, args=(animal, file, self._q1ToAI, self._q2FromAI, mazeSize[0], mazeSize[1], preparationTime, turnTime,))
        self._process.start()
            
        self._name = str(self._q2FromAI.get())
 
    # An AIPlayer plays (it is active)
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
            return (a,b)       
        
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
            
    def sendInfoForPreProcessing(self, otherPlayer_location, maze, pieces_of_cheese):
        self._q1ToAI.put((maze, self._location, otherPlayer_location, pieces_of_cheese))
    
    def sendInfoForATurn(self, otherPlayer_location, otherPlayer_Score, pieces_of_cheese):
        self._q1ToAI.put((self._location, otherPlayer_location, self._score, otherPlayer_Score, pieces_of_cheese)) 
        
    def sendInfoForPostProcessing(self, otherPlayer_location, otherPlayer_Score, pieces_of_cheese):
        self._q1ToAI.put((self._location, otherPlayer_location, self._score, otherPlayer_Score, pieces_of_cheese))     
        
    def quitGame(self, decision):
        self._q3Quit.put(decision)
        
    def getDecision(self, synchronous):
        return str(self._q2FromAI.get(synchronous))
    
    def sendEndingSignal(self):
        self._q1ToAI.put("stop")
    
    def processIsAlive(self):        
        return self._process.is_alive()
    
    # Ask to the AI to compute the new decision     
    def askForADecision(self, opponentLocation, opponentScore, piecesOfCheese):
        if self.canMove():
            self.sendInfoForATurn(opponentLocation, opponentScore, piecesOfCheese)
    
    # Demand AI to give right now its decision and to move according to it        
    def demandDecisionAndMove(self,synchronous,maze):
        try:
            decision = self.getDecision(synchronous)
        except:
            decision = "None"
            
        self.move(decision, maze)
        return decision   
        
    def computeDelays(self):
        while 1:
            res = self._q2FromAI.get()
            if res:
                self._prepDelay, self._turnDelay = res
                break
            time.sleep(0.1)    
            
    def stopAIProcess(self):
        if self.processIsAlive():
            try:
                for i in range(5):
                    self.putQInTrue()
            except:
                ()        
        # If it is still not dead, ask it gently to stop
        time.sleep(0.1)
        if self.processIsAlive():
            try:
                self._process.terminate()
            except:
                ()        
        # If it is still not dead, kill it
        time.sleep(0.1)
        while self.processIsAlive():
            os.kill(self._process.pid, signal.SIGKILL)
            time.sleep(0.01)        

                   
            
