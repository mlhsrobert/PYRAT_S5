from core.parameters import *
import time

class TestTool:
    
    def __init__(self):
        self.__minutesfile = ""
        self.__ratFile = ""
        self.__pythonFile = ""
        
    def saveInitialInfo(self, pieces_of_cheese, ratLocation, pythonLocation):
        if args.test_file:
            self.__minutesfile = open("testFiles/minutesFiles/NewMinutesFile",'w')
            self.__minutesfile.write("# Information for each turn : 1/piecesOfCheese, 2/rat Information 3/python Information\n")
            self.__minutesfile.write("# Information for each player : decision - location - score - moves - miss - mud\n")
            self.__minutesfile.write("# Initial information\n")
            self.__minutesfile.write(str(pieces_of_cheese)+"\n")
            self.__minutesfile.write("No decision to take - " + str(ratLocation)+"\n")
            self.__minutesfile.write("No decision to take - " + str(pythonLocation)+"\n")
            
            self.__ratFile = open("testFiles/pathFiles/Rat_NewPathFile",'w')
            self.__pythonFile = open("testFiles/pathFiles/Python_NewPathFile",'w')
            self.__ratFile.write("[")
            self.__pythonFile.write("[")            
            
    def saveTurn(self, turns, ratInfo, ratDecision, pythonInfo, pythonDecision, pieces_of_cheese):
        if args.test_file:
            (ratLocation, (ratScore, ratMoves, ratMiss, ratMud)) = ratInfo
            (pythonLocation, (pythonScore, pythonMoves, pythonMiss, pythonMud)) = pythonInfo
            self.__minutesfile.write("# turn "+str(turns) +"\n")
            self.__minutesfile.write(str(pieces_of_cheese) + "\n")
            self.__minutesfile.write(str(ratDecision)+" - "+ str(ratLocation) + " - " + str(ratScore) + " - " + str(ratMoves) + " - "+str(ratMiss) + " - " + str(ratMud) +"\n")
            self.__minutesfile.write(str(pythonDecision)+" - "+str(pythonLocation) + " - " + str(pythonScore) + " - " + str(pythonMoves) + " - "+str(pythonMiss) + " - " + str(pythonMud) + "\n")
            
            if str(ratDecision) != "None":
                self.__ratFile.write("'" +str(ratDecision)+"',")
            if str(pythonDecision) != "None":
                self.__pythonFile.write("'"+str(pythonDecision)+"',")
            
    def saveEndGame(self, turns, ratInfo, pythonInfo, pieces_of_cheese):
        if args.test_file:
            (ratLocation, (ratScore, ratMoves, ratMiss, ratMud)) = ratInfo
            (pythonLocation, (pythonScore, pythonMoves, pythonMiss, pythonMud)) = pythonInfo
            self.__minutesfile.write("# End game\n")
            self.__minutesfile.write(str(pieces_of_cheese) + "\n")
            self.__minutesfile.write("No decision to take - "+ str(ratLocation) + " - " + str(ratScore) + " - " + str(ratMoves) + " - "+str(ratMiss) + " - " + str(ratMud) +"\n")
            self.__minutesfile.write("No decision to take - "+str(pythonLocation) + " - " + str(pythonScore) + " - " + str(pythonMoves) + " - "+str(pythonMiss) + " - " + str(pythonMud) + "\n")
                      
            self.__ratFile.write("]")
            self.__pythonFile.write("]")        