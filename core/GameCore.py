#!/usr/bin/python
#    Copyright © 2017 Vincent Gripon (vincent.gripon@imt-atlatique.fr) and IMT Atlantique
#
#    This file is part of PyRat.
#
#    PyRat is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PyRat is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PyRat.  If not, see <http://www.gnu.org/licenses/>.

# Imports
from core.parameters import *
import sys
import time
import pygame
from util.soundManager import *
from player.Player import *
from util.Stats import *
from util.saveToolBox import *
from core.MazeInfo import *
from core.MazeGenerator import *
from display.DisplayController import *
from core.PlayerFactory import *
from util.TestToolBox import *

from importlib import import_module
    
class GameCore():
    
    def __init__(self):
        # This class represents the core of the game. It handles player turns, interactions with players and the display
        
        #self.__sound handles the sound
        self.__sound = SoundManager()
        
        #self.__saveFile saves information about the game
        self.__saveFile = Save()
        
        #self.__testFile saves information only about location and decision of players. Useful to do non-regression tests
        self.__testFile = TestTool()
        
        #self.__stats contains statistics of the game
        self.__stats = Stats()
        
        #self.__ratPlayer and self.__pythonPlayer represent the players. 
        #Here, there are initialized as InactivePlayer
        self.__ratPlayer = PlayerFactory.createPlayer("rat", "", (0,0), False, (3,3), 2000, 100)
        self.__pythonPlayer = PlayerFactory.createPlayer("python", "", (0,0), False, (3,3),2000, 100)   
        
        #self.__mazeInfo contains a maze with cheese and information about it
        self.__mazeInfo = MazeGenerator.generateMaze(3, 3, 0.7, True, True, 0, 10, "", 0, 1, False)  
        
        #self.__turns is the number of turns in a match of the game
        self.__turns = 0
        
        #self.__nbOfMatch is the number of matchs in the game
        self.__nbOfMatch = args.matches
        
    # GET
    def getRatPlayer(self):
        return self.__ratPlayer
    
    def getPythonPlayer(self):
        return self.__pythonPlayer
        
    def getMazeInfo(self):
        return self.__mazeInfo
    
    def getStats(self):
        return self.__stats.getStats()    
        
    #This function returns a boolean. If True, then it is the end of the match. If False, it is not.
    def isTheEndOfMatch(self):
        
        ratScore = self.__ratPlayer.getScore()
        pythonScore = self.__pythonPlayer.getScore()
        initialNbPiecesCheese = self.__mazeInfo.getInitialNbPiecesCheese()
        pieces_of_cheese = self.__mazeInfo.getPiecesOfCheese()
        
        #There are several possibilities to be at the end of the game
        
        #If the rat and the player are playing (as AI or human)
        if self.__ratPlayer.plays() and self.__pythonPlayer.plays():
            #The rat and the python have the same score and all pieces of cheese are eaten
            if ratScore == pythonScore and ratScore >= initialNbPiecesCheese / 2.0:
                self.__display.sendEndGameMessage("both")
                return True
            #The rat has eaten more than the half of pieces of cheese
            if ratScore > initialNbPiecesCheese / 2.0:
                self.__display.sendEndGameMessage("rat")
                return True
            #The python has eaten more than the half of pieces of cheese
            if pythonScore > initialNbPiecesCheese / 2.0:
                self.__display.sendEndGameMessage("python")
                return True
        #The rat or the python is playin alone    
        else:
            #The rat has eaten all pieces of cheese
            if ratScore >= initialNbPiecesCheese:
                self.__display.sendEndGameMessage("ratOnly")
                return True
            #The python has eaten all pieces of cheese
            elif pythonScore >= initialNbPiecesCheese:
                self.__display.sendEndGameMessage("pythonOnly")
                return True
        # There is no more cheese (this case never should happen without previous cases ??)
        if len(pieces_of_cheese) == 0:
            self.__display.sendEndGameMessage("cheese")
            return True
        return False
    
    #This function initialize the attributs at the beginning of each match of the game
    def initMatch(self, screen, infoObject):
        
        debug("Init the match",1)
        self.__turns = 0
        
        # Generate maze
        debug("Generating maze",1)
        
        if not(args.random_seed):
            random_seed = random.randint(0,sys.maxsize)
        else:
            random_seed = args.random_seed
        #print("Using seed " + str(random_seed), file=sys.stderr)
        
        self.__mazeInfo = MazeGenerator.generateMaze(args.width, args.height, args.density, not(args.nonconnected), 
                        not(args.nonsymmetric), args.mud_density, args.mud_range, 
                        args.maze_file, random_seed, args.pieces, args.start_random)
        
        #The following line is usefull if you want to save the maze in a file for a later use
        #MazeGenerator.generate_file_from_maze(self.__mazeInfo)
            
        if args.random_cheese:
            random.seed()
            
        # Create players
        debug("Create players",1)
        self.__ratPlayer = PlayerFactory.createPlayer("rat", args.rat, (0,0), args.start_random, self.__mazeInfo.getMazeSize(), args.preparation_time, args.turn_time)
        self.__pythonPlayer = PlayerFactory.createPlayer("python", args.python, (self.__mazeInfo.getMazeSize()[0]-1, self.__mazeInfo.getMazeSize()[1]-1), args.start_random, self.__mazeInfo.getMazeSize(),args.preparation_time, args.turn_time) #(self.__mazeInfo.getWidth()-1, self.__mazeInfo.getHeight()-1)        
        
        self.__saveFile.saveInitialInfo(random_seed, self.__mazeInfo.getMaze(), self.__mazeInfo.getPiecesOfCheese(), self.__ratPlayer.getLocation(), self.__pythonPlayer.getLocation())        
        self.__testFile.saveInitialInfo(self.__mazeInfo.getPiecesOfCheese(), self.__ratPlayer.getLocation(), self.__pythonPlayer.getLocation())
        
        # Create display
        debug("Create display",1)
        self.__display = DisplayController(screen, infoObject, self.__mazeInfo, self.__ratPlayer, self.__pythonPlayer)
    
    #This function checks if the players are on a piece of cheese and increase the score if so and plays sound            
    def checkCheese(self):
        
        ratOnCheese = self.__ratPlayer.isOnAPieceOfCheese(self.__mazeInfo)
        pythonOnCheese = self.__pythonPlayer.isOnAPieceOfCheese(self.__mazeInfo)
        
        if ratOnCheese:
            self.__mazeInfo.removeAPieceOfCheese(self.__ratPlayer.getLocation())
            #The rat and the python are on a piece of cheese
            if pythonOnCheese:
                #The rat and the python are on the same piece of cheese
                if self.__pythonPlayer.getLocation() == self.__ratPlayer.getLocation():
                    self.__ratPlayer.gotHalfPieceOfCheese()
                    self.__pythonPlayer.gotHalfPieceOfCheese()
                #The rat and the python are on a different piece of cheese
                else :
                    self.__mazeInfo.removeAPieceOfCheese(self.__pythonPlayer.getLocation())
                    self.__ratPlayer.gotPieceOfCheese()
                    self.__pythonPlayer.gotPieceOfCheese()
                self.__sound.playSoundBoth()
            #Only the rat is on a piece of cheese
            else:                
                self.__ratPlayer.gotPieceOfCheese()
                self.__sound.playSoundLeft()
        #Only the python is on a piece of cheese
        elif pythonOnCheese:
            self.__mazeInfo.removeAPieceOfCheese(self.__pythonPlayer.getLocation())
            self.__pythonPlayer.gotPieceOfCheese()
            self.__sound.playSoundRight()
    
    #This function returns True if the next turn has to be played. 
    #If so, the number of turns is increased and we reduce the stuck turns of the players    
    def nextTurn(self):
        # Check if the maximum of turns is not reached
        if self.__turns == args.max_turns:
            self.__display.sendEndGameMessage("turns")
            return False
        self.__turns +=1

        # If players are stuck with mud, this is one turn towards getting out of it
        self.__ratPlayer.reduceStuckTurns()
        self.__pythonPlayer.reduceStuckTurns()
        
        return True
    
    
    #This function runs the game. 
    def run(self, screen, infoObject):
        print("match 1" + "/" + str(self.__nbOfMatch))
        #stopFromDisplay allows to know if the match ends normaly or if it is because the human wants to leave.
        #If so, the other matchs should not be played
        stopFromDisplay = self.runMatch(screen, infoObject)
        if not stopFromDisplay:
            # Run other games (if any)
            for i in range(self.__nbOfMatch - 1):
                debug("Starting match number " + str(i))
                print("match " + str(i+2) + "/" + str(self.__nbOfMatch))
                stopFromDisplay = self.runMatch(screen, infoObject)
                if stopFromDisplay:
    
                    break  
                
    
    # This is the core function that runs a match. 
    # Returns False if the game stops normally and True if the human asks to quit the game
    def runMatch(self,screen, infoObject):
        debug("Run a match")
        self.initMatch(screen, infoObject)
           
        maze = self.__mazeInfo.getMaze()
       
        # Send initial information to players
        debug("Send initial information to players and start preprocessing",1)
        self.__ratPlayer.sendInfoForPreProcessing(self.__pythonPlayer.getLocation(), maze, self.__mazeInfo.getPiecesOfCheese())
        self.__pythonPlayer.sendInfoForPreProcessing(self.__ratPlayer.getLocation(), maze, self.__mazeInfo.getPiecesOfCheese())
       
        # Let time to preprocess
        if not(args.synchronous):
            time.sleep(args.preparation_time / 1000.0)        
    
        # Main loop
        debug("Starting match",1)
        while 1:
            
            if not self.nextTurn():
                break
                      
            # Check if one of the players is on a piece of cheese
            self.checkCheese()
    
            # Send drawing informations to graphical interface
            self.__display.sendDrawingInfo(self.__mazeInfo.getPiecesOfCheese(), self.__ratPlayer.getDisplayInformation(), self.__pythonPlayer.getDisplayInformation())
            
            #Check if it is the end of the match
            if self.isTheEndOfMatch():
                self.__testFile.saveEndGame( self.__turns, self.__ratPlayer.getDisplayInformation(), self.__pythonPlayer.getDisplayInformation(), self.__mazeInfo.getPiecesOfCheese())                
                break
            
            # Check if graphical interface wants us to exit the game
            if self.__display.stopFromDisplay():
                break
    
            # Magic solver for windows problems (does not like pygame in threads)
            pygame.event.pump()
            
            # Ask players to compute their next decision
            self.__ratPlayer.askForADecision(self.__pythonPlayer.getLocation(), self.__pythonPlayer.getScore(), self.__mazeInfo.getPiecesOfCheese())
            self.__pythonPlayer.askForADecision(self.__ratPlayer.getLocation(), self.__ratPlayer.getScore(), self.__mazeInfo.getPiecesOfCheese())
            
            self.__saveFile.saveTurn(self.__turns, self.__ratPlayer.getLocation(), self.__pythonPlayer.getLocation(), self.__mazeInfo.getPiecesOfCheese())
    
            # Wait for the turn to end
            if not(args.synchronous):
                time.sleep(args.turn_time / 1000.0)
            
            # Ask players to move according to their decision
            decision1 = self.__ratPlayer.demandDecisionAndMove(args.synchronous, maze)
            decision2 = self.__pythonPlayer.demandDecisionAndMove(args.synchronous, maze)
            
            self.__saveFile.saveDecisions(decision1, decision2)
            self.__testFile.saveTurn( self.__turns, self.__ratPlayer.getDisplayInformation(), decision1, self.__pythonPlayer.getDisplayInformation(), decision2, self.__mazeInfo.getPiecesOfCheese())
            
        # Now the game is finished, send ending signals to players 
        self.__ratPlayer.sendEndingSignal()
        self.__pythonPlayer.sendEndingSignal()
        
        
        # Send information for the post processing
        self.__ratPlayer.sendInfoForPostProcessing(self.__pythonPlayer.getLocation(), self.__pythonPlayer.getScore(), self.__mazeInfo.getPiecesOfCheese())
        self.__pythonPlayer.sendInfoForPostProcessing(self.__ratPlayer.getLocation(), self.__ratPlayer.getScore(), self.__mazeInfo.getPiecesOfCheese())
       
        #Compute informations about delays
        self.__ratPlayer.computeDelays()
        self.__pythonPlayer.computeDelays()     
                    
        # Stop the AI process
        try:
            self.__ratPlayer.stopAIProcess()      
            self.__pythonPlayer.stopAIProcess()             
        except:
            ()
                       
        # Stop the graphical interface
        self.__display.stopGraphicalInterface()
        
        # Send stats about the game
        #TODO : doit-on ajouter si le match n'est pas fini mais qu'on quitte avant ?
        matchStat = self.__stats.addResult(self.__ratPlayer, self.__pythonPlayer)
        
        self.__saveFile.saveStat(matchStat)
        
        return self.__display.getStopFromDisplay()
