from core.parameters import *
import time

class Save:
    
    def __init__(self):
        self.__savefile = ""
        
    def saveInitialInfo(self, random_seed, maze, pieces_of_cheese, ratLocation, pythonLocation):
        if args.save:
            self.__savefile = open("saves/"+str(int(round(time.time() * 1000))),'w')
            self.__savefile.write("# Random seed\n")
            self.__savefile.write(str(random_seed)+"\n")
            self.__savefile.write("# MazeMap\n")
            self.__savefile.write(str(maze)+"\n")
            self.__savefile.write("# Pieces of cheese\n")
            self.__savefile.write(str(pieces_of_cheese)+"\n")
            self.__savefile.write("# Rat initial location\n")
            self.__savefile.write(str(ratLocation)+"\n")
            self.__savefile.write("# Python initial location\n")
            self.__savefile.write(str(pythonLocation)+"\n")
            
    def saveTurn(self, turns, ratLocation, pythonLocation, pieces_of_cheese):
        if args.save:
            self.__savefile.write("# turn "+str(turns) + " rat_location then python_location then pieces_of_cheese then rat_decision then python_decision\n")
            self.__savefile.write(str(ratLocation) + "\n")
            self.__savefile.write(str(pythonLocation) + "\n")
            self.__savefile.write(str(pieces_of_cheese) + "\n")
            
    def saveDecisions(self, decision1, decision2):
        if args.save:
            self.__savefile.write(decision1 + "\n")
            self.__savefile.write(decision2 + "\n")
            
    def saveStat(self, matchStat):
        if args.save:
            self.__savefile.write(str(matchStat))
            self.__savefile.close()        