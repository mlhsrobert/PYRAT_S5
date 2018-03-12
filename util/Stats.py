from player.Player import *

class Stats:   

    
    def __init__(self):
        self.__rat_Score = 0.
        self.__python_Score = 0.
        self.__rat_Moves = 0.
        self.__python_Moves = 0.
        self.__rat_MissedTurns = 0.
        self.__python_MissedTurns = 0.
        self.__rat_MudFences = 0.
        self.__python_MudFences = 0.
        self.__rat_PrepDelay = 0.
        self.__python_PrepDelay = 0.
        self.__rat_TurnDelay = 0.
        self.__python_TurnDelay = 0.
        self.__rat_Victories = 0.
        self.__python_Victories = 0.
        self.__numberOfMatchs = 0.       
        
    def addResult(self, ratPlayer, pythonPlayer):
        
        ratScore, ratMoves, ratMiss, ratMud, ratPrepDelay, ratTurnDelay = ratPlayer.getStatsInformation()
        pythonScore, pythonMoves, pythonMiss, pythonMud, pythonPrepDelay, pythonTurnDelay = pythonPlayer.getStatsInformation()
        
        
        self.__numberOfMatchs += 1
        
        if ratScore == pythonScore:
            self.__rat_Victories += 0.5
            ratWin = 0.5
            self.__python_Victories += 0.5
            pythonWin = 0.5
        elif ratScore > pythonScore:
            self.__rat_Victories += 1
            ratWin = 1
            pythonWin = 0
        else:
            self.__python_Victories += 1
            pythonWin = 1
            ratWin = 0
           
        self.__rat_Score += ratScore
        self.__python_Score += pythonScore
        self.__rat_Moves += ratMoves
        self.__python_Moves += pythonMoves
        self.__rat_MissedTurns += ratMiss
        self.__python_MissedTurns += pythonMiss
        self.__rat_MudFences += ratMud
        self.__python_MudFences += pythonMud
        self.__rat_PrepDelay += ratPrepDelay
        self.__python_PrepDelay += pythonPrepDelay
        self.__rat_TurnDelay += ratTurnDelay
        self.__python_TurnDelay += pythonTurnDelay
        
        matchStat = {"Rat_victories": ratWin, "Python_victories": pythonWin,
                     "score_rat": ratScore, "score_python": pythonScore, 
                     "moves_rat": ratMoves, "moves_python": pythonMoves, 
                     "miss_rat": ratMiss, "miss_python": pythonMiss, 
                     "stucks_rat":ratMud, "stucks_python": pythonMud, 
                     "prep_time_rat":ratPrepDelay, "prep_time_python":pythonPrepDelay, 
                     "turn_time_rat":ratTurnDelay, "turn_time_python":pythonTurnDelay}
        return matchStat
                
    def getStats(self):
        if(self.__numberOfMatchs > 0):
            stats = {"Rat_victories": self.__rat_Victories, "Python_victories": self.__python_Victories, 
                     "score_rat": self.__rat_Score/self.__numberOfMatchs, "score_python": self.__python_Score/self.__numberOfMatchs, 
                     "moves_rat": self.__rat_Moves/self.__numberOfMatchs, "moves_python": self.__python_Moves/self.__numberOfMatchs, 
                     "miss_rat": self.__rat_MissedTurns/self.__numberOfMatchs, "miss_python": self.__python_MissedTurns/self.__numberOfMatchs, 
                     "stucks_rat":self.__rat_MudFences/self.__numberOfMatchs, "stucks_python":self.__python_MudFences/self.__numberOfMatchs, 
                     "prep_time_rat":self.__rat_PrepDelay/self.__numberOfMatchs, "prep_time_python":self.__python_PrepDelay/self.__numberOfMatchs, 
                     "turn_time_rat":self.__rat_TurnDelay/self.__numberOfMatchs, "turn_time_python":self.__python_TurnDelay/self.__numberOfMatchs}
        else:
            stats = {"No match" : 0}
        return stats