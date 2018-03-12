from player.Player import *
from player.AIPlayer import *
from core.PlayerFactory import *
from util.errors import *
from core.MazeInfo import *
from core.MazeGenerator import *

import multiprocessing

mazeInfo = MazeGenerator.generateMaze(10, 10, 0.3, True, True, 0.3, 0.3, "maze_files/Maze1.maze", 0.2, 5, False)


#TEST FOR PLAYER
def PlayerTests():
    print("TEST FOR CLASS PLAYER")
    giveResult(PlayerTests_argstest())
    giveResult(PlayerTests_testInit())

def PlayerTests_argstest():
    print("TEST -- PlayerTests_argstest :")
    succes = True

    #Tests for the arguments
    try:
        Player((0,0), False, True)
        print("-->Test 1 : ArgsException should occurre, mazeSize is not a tuple")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        Player((0,0), False, (True,10))
        print("-->Test 2 : ArgsException should occurre, mazeSize is not a tuple of int")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        Player((0,0), False, (10,"ok"))
        print("-->Test 3 : ArgsException should occurre, mazeSize is not a tuple of int")
        succes = False
    except ArgsException as e:
        ()        
        
    try:
        Player((0,0), False, (-1,10))
        print("-->Test 4 : ArgsException should occurre, mazeSize is negative")
        succes = False
    except ArgsException as e:
        ()   
        
    try:
        Player((0,0), False, (1,-10))
        print("-->Test 5 : ArgsException should occurre, mazeSize is negative")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        Player(False, False, (10,10))
        print("-->Test 6 : ArgsException should occurre, location is not a tuple")
        succes = False
    except ArgsException as e:
        ()    

    try:
        Player((False,1), False, (10,10))
        print("-->Test 7 : ArgsException should occurre, location is not a tuple of int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        Player((1,"ok"), False, (10,10))
        print("-->Test 8 : ArgsException should occurre, location is not a tuple of int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        Player((-1,9), False, (10,10))
        print("-->Test 9 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        Player((9,-10), False, (10,10))
        print("-->Test 10 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        ()  
        
    try:
        Player((100,9), False, (10,10))
        print("-->Test 11 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        Player((9,100), False, (10,10))
        print("-->Test 12 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        ()         

    try:
        Player((0,0), 1, (10,10))
        print("-->Test 13 : ArgsException should occurre, randomStart is not a boolean")
        succes = False
    except ArgsException as e:
        () 
    return succes


def PlayerTests_testInit():
    print("TEST -- testInit :")
    succes = True
    
    try:
        player = Player((0,0), False, (10,10))
    except ArgsException as e:
        print("-->Test 0 : ArgsException occurred but should not. Value :", e)
               
    score = player._score
    stuckTurns = player._stuckTurns
    moves = player._moves
    miss = player._miss
    mud = player._mud
    prepDelay = player._prepDelay
    turnDelay = player._turnDelay
    location = player._location
    name = player._name 
    
    if type(score) != float or score != 0.:
        print("-->Test 1 : Error with score. \n Received : " + str(score) + " (" +str(type(score))+")")
        succes = False
    if type(stuckTurns) != int or stuckTurns != 0:
        print("-->Test 2 : Error with stuckTurns. \n Received : " + str(stuckTurns) + " (" +str(type(stuckTurns))+")")
        succes = False
    if type(moves) != int or moves != 0:
        print("-->Test 3 : Error with moves. \n Received : " + str(moves) + " (" +str(type(moves))+")")
        succes = False
    if type(miss) != int or miss != 0:
        print("-->Test 4 : Error with miss. \n Received : " + str(miss) + " (" +str(type(miss))+")")
        succes = False 
    if type(mud) != int or mud != 0:
        print("-->Test 5 : Error with mud. \n Received : " + str(mud) + " (" +str(type(mud))+")")
        succes = False 
    if type(prepDelay) != float or prepDelay != 0.:
        print("-->Test 6 : Error with prepDelay. \n Received : " + str(prepDelay) + " (" +str(type(prepDelay))+")")
        succes = False 
    if type(turnDelay) != float or turnDelay != 0.:
        print("-->Test 7 : Error with turnDelay. \n Received : " + str(turnDelay) + " (" +str(type(turnDelay))+")")
        succes = False 
    if (type(location) != tuple) or (type(location[0]) != int) or (type(location[1]) != int) or (location != (0,0)):
        print("-->Test 8 : Error with location. \n Received : " + str(location) + " (" +str(type(location))+")")
        succes = False         
    if type(name) != str or name != "no name":
        print("-->Test 9 : Error with name. \n Received : " + str(name) + " (" +str(type(name))+")")
        succes = False        
    
    try:
        player = Player((9,9), True, (10,10))
    except ArgsException as e:
        print("-->Test 10 : ArgsException occurred but should not. Value :", e) 
        succes = False
        
    location = player._location   
        
    if (type(location) != tuple) or (type(location[0]) != int) or (type(location[1]) != int) or (location[0]<0) or (location[0]>=10) or (location[1]<0) or (location[1]>=10):
        print("-->Test 11 : Error with location. \n Received : " + str(location) + " (" +str(type(location))+")")
        succes = False 
         
    
    return succes

def AIPlayerTests():
    print("TEST FOR CLASS AIPLAYER")
    giveResult(AIPlayerTests_argstest())
    giveResult(AIPlayerTests_testInit())
    giveResult(AIPlayerTests_testMoveFunctions())
    
def AIPlayerTests_argstest():
    print("TEST -- AIPlayerTests_argstest :")
    succes = True

    #Tests for the arguments
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,0), False, 10, 100, 200)
        print("-->Test 1 : ArgsException should occurre, mazeSize is not a tuple")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,0), False, (True,10), 100, 200)
        print("-->Test 2 : ArgsException should occurre, mazeSize is not a tuple of int")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,"ok"), 100, 200)
        print("-->Test 3 : ArgsException should occurre, mazeSize is not a tuple of int")
        succes = False
    except ArgsException as e:
        ()        
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,0), False, (-10,10), 100, 200)
        print("-->Test 4 : ArgsException should occurre, mazeSize is negative")
        succes = False
    except ArgsException as e:
        ()   
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,-10), 100, 200)
        print("-->Test 5 : ArgsException should occurre, mazeSize is negative")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", False, False, (10,10), 100, 200)
        print("-->Test 6 : ArgsException should occurre, location is not a tuple")
        succes = False
    except ArgsException as e:
        ()    

    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,True), False, (10,10), 100, 200)
        print("-->Test 7 : ArgsException should occurre, location is not a tuple of int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", ("ok",0), False, (10,10), 100, 200)
        print("-->Test 8 : ArgsException should occurre, location is not a tuple of int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (-10,0), False, (10,10), 100, 200)
        print("-->Test 9 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,-10), False, (10,10), 100, 200)
        print("-->Test 10 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        ()  
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (10,0), False, (10,10), 100, 200)
        print("-->Test 11 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,10), False, (10,10), 100, 200)
        print("-->Test 12 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        ()         

    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,0), 0, (10,10), 100, 200)
        print("-->Test 13 : ArgsException should occurre, randomStart is not a boolean")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        AIPlayer(1010, "AIs/RatTest.py", (0,0), False, (10,10), 100, 200)
        print("-->Test 14 : ArgsException should occurre, animal is not a string")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        AIPlayer("rat", 5658, (0,0), False, (10,10), 100, 200)
        print("-->Test 15 : ArgsException should occurre, file is not a string")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,10), False, 200)
        print("-->Test 16 : ArgsException should occurre, preparationTime is not a int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,10), -100, 200)
        print("-->Test 17 : ArgsException should occurre, preparationTime is not negative")
        succes = False
    except ArgsException as e:
        ()         
             
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,10), 100, "hello")
        print("-->Test 18 : ArgsException should occurre, turnTime is not a int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        AIPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,10), 100, -200)
        print("-->Test 19 : ArgsException should occurre, turnTime is not negative")
        succes = False
    except ArgsException as e:
        ()         
             
    return succes

def AIPlayerTests_testInit():
    print("TEST -- AIPlayerTests_testInit :")
    succes = True
    
    try:
        player = AIPlayer("rat", "AIs/Test_Rat1.py", (0,0), False, (10,10), 100, 200)
    except ArgsException as e:
        print("-->Test 0 : ArgsException occurred but should not. Value :", e) 
    
    if type(player._q1ToAI) != multiprocessing.queues.Queue:
        print("-->Test 1 : Error with player._q1ToAI. \n Received : " + str(player._q1ToAI) + " (" +str(type(player._q1ToAI))+")")
        succes = False
    if type(player._q2FromAI) != multiprocessing.queues.Queue:
        print("-->Test 2 : Error with player._q2FromAI. \n Received : " + str(player._q2FromAI) + " (" +str(type(player._q2FromAI))+")")
        succes = False
    if type(player._process) != multiprocessing.context.Process:
        print("-->Test 3 : Error with player._process. \n Received : " + str(player._process) + " (" +str(type(player._process))+")")
        succes = False          
    if type(player._name) != str or player._name != "Triple-patte":
        print("-->Test 4 : Error with name. \n Received : " + str(player._name) + " (" +str(type(player._name))+")")
        succes = False 
        
    try:
        player = AIPlayer("rat", "InexistantFile", (0,0), False, (10,10), 100, 200)
    except ArgsException as e:
        print("-->Test 5 : ArgsException occurred but should not. Value :", e)     
    
    if type(player._name) != str or player._name != "Dummy":
        print("-->Test 6 : Error with name. \n Received : " + str(player._name) + " (" +str(type(player._name))+")")
        succes = False    

    return succes  

def AIPlayerTests_testMoveFunctions():
    print("TEST -- AIPlayerTests_testMoveFunctions :")
    succes = True 
    
    player = AIPlayer("rat", "AIs/Test_Rat1.py", (0,0), False, (10,10), 100, 200)
    
    #Test cellOfDecision
    cell = player.cellOfDecision("U")
    if cell != (0,1):
        print("-->Test 1 : Error with cellOfDecision(U). \n Result : " + str(cell) + " instead of (0,1)")
        succes = False
    cell = player.cellOfDecision("D")
    if cell != (0,-1):
        print("-->Test 2 : Error with cellOfDecision(D). \n Result : " + str(cell) + " instead of (0,-1)")
        succes = False
    cell = player.cellOfDecision("L")
    if cell != (-1,0):
        print("-->Test 3 : Error with cellOfDecision(L). \n Result : " + str(cell) + " instead of (-1,0)")  
        succes = False
    cell = player.cellOfDecision("R")
    if cell != (1,0):
        print("-->Test 4 : Error with cellOfDecision(R). \n Result : " + str(cell) + " instead of (1,0)")  
        succes = False
    cell = player.cellOfDecision("None")
    if cell != (0,0):
        print("-->Test 5 : Error with cellOfDecision(None). \n Result : " + str(cell) + " instead of (0,0)")  
        succes = False
    cell = player.cellOfDecision("invalid")
    if cell != (0,0):
        print("-->Test 6 : Error with cellOfDecision(invalid). \n Result : " + str(cell) + " instead of (0,0)")
        succes = False
    cell = player.cellOfDecision(300)
    if cell !=(0,0):
        print("-->Test 7 : Error with cellOfDecision(300). \n Result : " + str(cell) + " instead of (0,0)")
        succes = False
        
    player.reduceStuckTurns()    
    player.move("L",mazeInfo.getMaze())
    if player.getStuckTurns() != -1:
        print("-->Test 8 : Error with move. : " + "Result : " + str(player.getStuckTurns()) + " instead of -1")
        succes = False
    if player.getLocation() != (0,0):
        print("-->Test 9 : Error with move. : " + "Result : " + str(player.getLocation()) + " instead of (0,0)")
        succes = False 
    if player.getMoves() != 0:
        print("-->Test 10 : Error with move. : " + "Result : " + str(player.getMoves()) + " instead of 0")
        succes = False   
    if player.getMissedTurns() != 1:
        print("-->Test 11 : Error with move. : " + "Result : " + str(player.getMissedTurns()) + " instead of 1")
        succes = False
    if player.getMudFence() != 0:
        print("-->Test 12 : Error with move. : " + "Result : " + str(player.getMudFence()) + " instead of 0")
        succes = False    
    
    player.reduceStuckTurns()     
    player.move("R",mazeInfo.getMaze())
    if player.getStuckTurns() != 1:
        print("-->Test 13 : Error with move. : " + "Result : " + str(player.getStuckTurns()) + " instead of 1")
        succes = False
    if player.getLocation() != (1,0):
        print("-->Test 14 : Error with move. : " + "Result : " + str(player.getLocation()) + " instead of (1,0)")
        succes = False 
    if player.getMoves() != 1:
        print("-->Test 15 : Error with move. : " + "Result : " + str(player.getMoves()) + " instead of 1")
        succes = False   
    if player.getMissedTurns() != 1:
        print("-->Test 16 : Error with move. : " + "Result : " + str(player.getMissedTurns()) + " instead of 1")
        succes = False
    if player.getMudFence() != 0:
        print("-->Test 17 : Error with move. : " + "Result : " + str(player.getMudFence()) + " instead of 0")
        succes = False        
    
    player.reduceStuckTurns() 
    player.move("L",mazeInfo.getMaze())
    if player.getStuckTurns() != 1:
        print("-->Test 18 : Error with move. : " + "Result : " + str(player.getStuckTurns()) + " instead of 1")
        succes = False
    if player.getLocation() != (0,0):
        print("-->Test 19 : Error with move. : " + "Result : " + str(player.getLocation()) + " instead of (0,0)")
        succes = False 
    if player.getMoves() != 2:
        print("-->Test 20 : Error with move. : " + "Result : " + str(player.getMoves()) + " instead of 2")
        succes = False   
    if player.getMissedTurns() != 1:
        print("-->Test 21 : Error with move. : " + "Result : " + str(player.getMissedTurns()) + " instead of 1")
        succes = False 
    if player.getMudFence() != 0:
        print("-->Test 22 : Error with move. : " + "Result : " + str(player.getMudFence()) + " instead of 0")
        succes = False        
    
    player.reduceStuckTurns() 
    player.move("U",mazeInfo.getMaze())
    if player.getStuckTurns() != 1:
        print("-->Test 23 : Error with move. : " + "Result : " + str(player.getStuckTurns()) + " instead of 1")
        succes = False
    if player.getLocation() != (0,1):
        print("-->Test 24 : Error with move. : " + "Result : " + str(player.getLocation()) + " instead of (0,1)")
        succes = False 
    if player.getMoves() != 3:
        print("-->Test 25 : Error with move. : " + "Result : " + str(player.getMoves()) + " instead of 3")
        succes = False   
    if player.getMissedTurns() != 1:
        print("-->Test 26 : Error with move. : " + "Result : " + str(player.getMissedTurns()) + " instead of 1")
        succes = False 
    if player.getMudFence() != 0:
        print("-->Test 27 : Error with move. : " + "Result : " + str(player.getMudFence()) + " instead of 0")
        succes = False        
    
    player.reduceStuckTurns() 
    player.move("U",mazeInfo.getMaze())
    if player.getStuckTurns() != 1:
        print("-->Test 28 : Error with move. : " + "Result : " + str(player.getStuckTurns()) + " instead of 1")
        succes = False
    if player.getLocation() != (0,2):
        print("-->Test 29 : Error with move. : " + "Result : " + str(player.getLocation()) + " instead of (0,2)")
        succes = False 
    if player.getMoves() != 4:
        print("-->Test 30 : Error with move. : " + "Result : " + str(player.getMoves()) + " instead of 4")
        succes = False   
    if player.getMissedTurns() != 1:
        print("-->Test 31 : Error with move. : " + "Result : " + str(player.getMissedTurns()) + " instead of 1")
        succes = False 
    if player.getMudFence() != 0:
        print("-->Test 32 : Error with move. : " + "Result : " + str(player.getMudFence()) + " instead of 0")
        succes = False 
        
    player = AIPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,10), 100, 200)
    test = player.isOnAPieceOfCheese(mazeInfo)
    if test:
        print("-->Test 33 : Error with isOnAPieceOfCheese. : " + "Result : " + str(test) + " instead of False")
        succes = False 
        
    player._location = (9,0)
    player._stuckTurns = 2
    test = player.isOnAPieceOfCheese(mazeInfo)
    if test:
        print("-->Test 34 : Error with isOnAPieceOfCheese. : " + "Result : " + str(test) + " instead of False")
        succes = False
        
    player._stuckTurns = -2
    test = player.isOnAPieceOfCheese(mazeInfo)
    if (test):
        print("-->Test 35 : Error with isOnAPieceOfCheese. : " + "Result : " + str(test) + " instead of False")
        succes = False    
    
        
    return succes

def HumanPlayerTests():
    print("TEST FOR HUMANPLAYER")
    giveResult(HumanPlayerTests_argstest())
    giveResult(HumanPlayerTests_testInit())
    giveResult(HumanPlayerTests_testMoveFunctions())
    
def HumanPlayerTests_argstest():
    print("TEST -- HumanPlayerTests_argstest :")
    succes = True

    #Tests for the arguments
    try:
        HumanPlayer((0,0), False, True)
        print("-->Test 1 : ArgsException should occurre, mazeSize is not a tuple")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        HumanPlayer((0,0), False, (True,10))
        print("-->Test 2 : ArgsException should occurre, mazeSize is not a tuple of int")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        HumanPlayer((0,0), False, (10,"ok"))
        print("-->Test 3 : ArgsException should occurre, mazeSize is not a tuple of int")
        succes = False
    except ArgsException as e:
        ()        
        
    try:
        HumanPlayer((0,0), False, (-1,10))
        print("-->Test 4 : ArgsException should occurre, mazeSize is negative")
        succes = False
    except ArgsException as e:
        ()   
        
    try:
        HumanPlayer((0,0), False, (1,-10))
        print("-->Test 5 : ArgsException should occurre, mazeSize is negative")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        HumanPlayer(False, False, (10,10))
        print("-->Test 6 : ArgsException should occurre, location is not a tuple")
        succes = False
    except ArgsException as e:
        ()    

    try:
        HumanPlayer((False,1), False, (10,10))
        print("-->Test 7 : ArgsException should occurre, location is not a tuple of int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        HumanPlayer((1,"ok"), False, (10,10))
        print("-->Test 8 : ArgsException should occurre, location is not a tuple of int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        HumanPlayer((-1,9), False, (10,10))
        print("-->Test 9 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        HumanPlayer((9,-10), False, (10,10))
        print("-->Test 10 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        ()  
        
    try:
        HumanPlayer((100,9), False, (10,10))
        print("-->Test 11 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        HumanPlayer((9,100), False, (10,10))
        print("-->Test 12 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        ()         

    try:
        HumanPlayer((0,0), 1, (10,10))
        print("-->Test 13 : ArgsException should occurre, randomStart is not a boolean")
        succes = False
    except ArgsException as e:
        () 
    return succes    

def HumanPlayerTests_testInit():
    print("TEST -- HumanPlayerTests_testInit :")
    succes = True
    
    try:
        player = HumanPlayer((0,0), False, (10,10))
    except ArgsException as e:
        print("-->Test 0 : ArgsException occurred but should not. Value :", e) 
    
    if type(player._qFromDisplay) != multiprocessing.queues.Queue:
        print("-->Test 1 : Error with player._qFromDisplay. \n Received : " + str(player._qFromDisplay) + " (" +str(type(player._qFromDisplay))+")")
        succes = False         
    if type(player._name) != str or player._name != "human":
        print("-->Test 2 : Error with name. \n Received : " + str(player._name) + " (" +str(type(player._name))+")")
        succes = False    

    return succes

def HumanPlayerTests_testMoveFunctions():
    print("TEST -- HumanPlayerTests_testMoveFunctions :")
    succes = True 
    
    player = HumanPlayer((0,0), False, (10,10))
    
    #Test cellOfDecision
    cell = player.cellOfDecision("U")
    if cell != (0,1):
        print("-->Test 1 : Error with cellOfDecision(U). \n Result : " + str(cell) + " instead of (0,1)")
        succes = False
    cell = player.cellOfDecision("D")
    if cell != (0,-1):
        print("-->Test 2 : Error with cellOfDecision(D). \n Result : " + str(cell) + " instead of (0,-1)")
        succes = False
    cell = player.cellOfDecision("L")
    if cell != (-1,0):
        print("-->Test 3 : Error with cellOfDecision(L). \n Result : " + str(cell) + " instead of (-1,0)")  
        succes = False
    cell = player.cellOfDecision("R")
    if cell != (1,0):
        print("-->Test 4 : Error with cellOfDecision(R). \n Result : " + str(cell) + " instead of (1,0)")  
        succes = False
    cell = player.cellOfDecision("None")
    if cell != (0,0):
        print("-->Test 5 : Error with cellOfDecision(None). \n Result : " + str(cell) + " instead of (0,0)")  
        succes = False
    try:
        cell = player.cellOfDecision("invalid")
        print("-->Test 6 : Error with cellOfDecision(invalid). An error should be raised but it did not \n Result : " + str(cell))
        succes = False
    except ArgsException:
        ()
    try:
        cell = player.cellOfDecision(300)
        print("-->Test 7 : Error with cellOfDecision(300). An error should be raised but it did not \n Result : " + str(cell))
        succes = False
    except ArgsException:
        () 
        
    player.reduceStuckTurns()    
    player.move("L",mazeInfo.getMaze())
    if player.getStuckTurns() != -1:
        print("-->Test 8 : Error with move. : " + "Result : " + str(player.getStuckTurns()) + " instead of -1")
        succes = False
    if player.getLocation() != (0,0):
        print("-->Test 9 : Error with move. : " + "Result : " + str(player.getLocation()) + " instead of (0,0)")
        succes = False 
    if player.getMoves() != 0:
        print("-->Test 10 : Error with move. : " + "Result : " + str(player.getMoves()) + " instead of 0")
        succes = False   
    if player.getMissedTurns() != 1:
        print("-->Test 11 : Error with move. : " + "Result : " + str(player.getMissedTurns()) + " instead of 1")
        succes = False
    if player.getMudFence() != 0:
        print("-->Test 12 : Error with move. : " + "Result : " + str(player.getMudFence()) + " instead of 0")
        succes = False    
    
    player.reduceStuckTurns()     
    player.move("R",mazeInfo.getMaze())
    if player.getStuckTurns() != 1:
        print("-->Test 13 : Error with move. : " + "Result : " + str(player.getStuckTurns()) + " instead of 1")
        succes = False
    if player.getLocation() != (1,0):
        print("-->Test 14 : Error with move. : " + "Result : " + str(player.getLocation()) + " instead of (1,0)")
        succes = False 
    if player.getMoves() != 1:
        print("-->Test 15 : Error with move. : " + "Result : " + str(player.getMoves()) + " instead of 1")
        succes = False   
    if player.getMissedTurns() != 1:
        print("-->Test 16 : Error with move. : " + "Result : " + str(player.getMissedTurns()) + " instead of 1")
        succes = False
    if player.getMudFence() != 0:
        print("-->Test 17 : Error with move. : " + "Result : " + str(player.getMudFence()) + " instead of 0")
        succes = False        
    
    player.reduceStuckTurns() 
    player.move("L",mazeInfo.getMaze())
    if player.getStuckTurns() != 1:
        print("-->Test 18 : Error with move. : " + "Result : " + str(player.getStuckTurns()) + " instead of 1")
        succes = False
    if player.getLocation() != (0,0):
        print("-->Test 19 : Error with move. : " + "Result : " + str(player.getLocation()) + " instead of (0,0)")
        succes = False 
    if player.getMoves() != 2:
        print("-->Test 20 : Error with move. : " + "Result : " + str(player.getMoves()) + " instead of 2")
        succes = False   
    if player.getMissedTurns() != 1:
        print("-->Test 21 : Error with move. : " + "Result : " + str(player.getMissedTurns()) + " instead of 1")
        succes = False 
    if player.getMudFence() != 0:
        print("-->Test 22 : Error with move. : " + "Result : " + str(player.getMudFence()) + " instead of 0")
        succes = False        
    
    player.reduceStuckTurns() 
    player.move("U",mazeInfo.getMaze())
    if player.getStuckTurns() != 1:
        print("-->Test 23 : Error with move. : " + "Result : " + str(player.getStuckTurns()) + " instead of 1")
        succes = False
    if player.getLocation() != (0,1):
        print("-->Test 24 : Error with move. : " + "Result : " + str(player.getLocation()) + " instead of (0,1)")
        succes = False 
    if player.getMoves() != 3:
        print("-->Test 25 : Error with move. : " + "Result : " + str(player.getMoves()) + " instead of 3")
        succes = False   
    if player.getMissedTurns() != 1:
        print("-->Test 26 : Error with move. : " + "Result : " + str(player.getMissedTurns()) + " instead of 1")
        succes = False 
    if player.getMudFence() != 0:
        print("-->Test 27 : Error with move. : " + "Result : " + str(player.getMudFence()) + " instead of 0")
        succes = False        
    
    player.reduceStuckTurns() 
    player.move("U",mazeInfo.getMaze())
    if player.getStuckTurns() != 1:
        print("-->Test 28 : Error with move. : " + "Result : " + str(player.getStuckTurns()) + " instead of 1")
        succes = False
    if player.getLocation() != (0,2):
        print("-->Test 29 : Error with move. : " + "Result : " + str(player.getLocation()) + " instead of (0,2)")
        succes = False 
    if player.getMoves() != 4:
        print("-->Test 30 : Error with move. : " + "Result : " + str(player.getMoves()) + " instead of 4")
        succes = False   
    if player.getMissedTurns() != 1:
        print("-->Test 31 : Error with move. : " + "Result : " + str(player.getMissedTurns()) + " instead of 1")
        succes = False 
    if player.getMudFence() != 0:
        print("-->Test 32 : Error with move. : " + "Result : " + str(player.getMudFence()) + " instead of 0")
        succes = False 
        
    player = HumanPlayer((0,0), False, (10,10))
    test = player.isOnAPieceOfCheese(mazeInfo)
    if test:
        print("-->Test 33 : Error with isOnAPieceOfCheese. : " + "Result : " + str(test) + " instead of False")
        succes = False 
        
    player._location = (9,0)
    player._stuckTurns = 2
    test = player.isOnAPieceOfCheese(mazeInfo)
    if test:
        print("-->Test 34 : Error with isOnAPieceOfCheese. : " + "Result : " + str(test) + " instead of False")
        succes = False
        
    player._stuckTurns = -2
    test = player.isOnAPieceOfCheese(mazeInfo)
    if (test):
        print("-->Test 35 : Error with isOnAPieceOfCheese. : " + "Result : " + str(test) + " instead of False")
        succes = False    
    
        
    return succes

def InactivePlayerTests():
    print("TEST FOR HUMANPLAYER")
    giveResult(InactivePlayerTests_argstest())
    giveResult(InactivePlayerTests_testInit())
    
def InactivePlayerTests_argstest():
    print("TEST -- InactivePlayerTests_argstest :")
    succes = True

    #Tests for the arguments
    try:
        InactivePlayer((0,0), False, True)
        print("-->Test 1 : ArgsException should occurre, mazeSize is not a tuple")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        InactivePlayer((0,0), False, (True,10))
        print("-->Test 2 : ArgsException should occurre, mazeSize is not a tuple of int")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        InactivePlayer((0,0), False, (10,"ok"))
        print("-->Test 3 : ArgsException should occurre, mazeSize is not a tuple of int")
        succes = False
    except ArgsException as e:
        ()        
        
    try:
        InactivePlayer((0,0), False, (-1,10))
        print("-->Test 4 : ArgsException should occurre, mazeSize is negative")
        succes = False
    except ArgsException as e:
        ()   
        
    try:
        InactivePlayer((0,0), False, (1,-10))
        print("-->Test 5 : ArgsException should occurre, mazeSize is negative")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        InactivePlayer(False, False, (10,10))
        print("-->Test 6 : ArgsException should occurre, location is not a tuple")
        succes = False
    except ArgsException as e:
        ()    

    try:
        InactivePlayer((False,1), False, (10,10))
        print("-->Test 7 : ArgsException should occurre, location is not a tuple of int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        InactivePlayer((1,"ok"), False, (10,10))
        print("-->Test 8 : ArgsException should occurre, location is not a tuple of int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        InactivePlayer((-1,9), False, (10,10))
        print("-->Test 9 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        InactivePlayer((9,-10), False, (10,10))
        print("-->Test 10 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        ()  
        
    try:
        InactivePlayer((100,9), False, (10,10))
        print("-->Test 11 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        InactivePlayer((9,100), False, (10,10))
        print("-->Test 12 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        ()         

    try:
        InactivePlayer((0,0), 1, (10,10))
        print("-->Test 13 : ArgsException should occurre, randomStart is not a boolean")
        succes = False
    except ArgsException as e:
        () 
    return succes    

def InactivePlayerTests_testInit():
    print("TEST -- InactivePlayerTests_testInit :")
    succes = True
    
    try:
        player = InactivePlayer((0,0), False, (10,10))
    except ArgsException as e:
        print("-->Test 0 : ArgsException occurred but should not. Value :", e) 
        
    if type(player._name) != str or player._name != "InactivePlayer":
        print("-->Test 1 : Error with name. \n Received : " + str(player._name) + " (" +str(type(player._name))+")")
        succes = False    

    return succes

def PlayerFactoryTests():
    print("TEST FOR PLAYERFACTORY")
    
    succes = True

    #Tests for the arguments
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,0), False, 10, 100, 200)
        print("-->Test 1 : ArgsException should occurre, mazeSize is not a tuple")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,0), False, (True,10), 100, 200)
        print("-->Test 2 : ArgsException should occurre, mazeSize is not a tuple of int")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,"ok"), 100, 200)
        print("-->Test 3 : ArgsException should occurre, mazeSize is not a tuple of int")
        succes = False
    except ArgsException as e:
        ()        
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,0), False, (-10,10), 100, 200)
        print("-->Test 4 : ArgsException should occurre, mazeSize is negative")
        succes = False
    except ArgsException as e:
        ()   
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,-10), 100, 200)
        print("-->Test 5 : ArgsException should occurre, mazeSize is negative")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", False, False, (10,10), 100, 200)
        print("-->Test 6 : ArgsException should occurre, location is not a tuple")
        succes = False
    except ArgsException as e:
        ()    

    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,True), False, (10,10), 100, 200)
        print("-->Test 7 : ArgsException should occurre, location is not a tuple of int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", ("ok",0), False, (10,10), 100, 200)
        print("-->Test 8 : ArgsException should occurre, location is not a tuple of int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (-10,0), False, (10,10), 100, 200)
        print("-->Test 9 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,-10), False, (10,10), 100, 200)
        print("-->Test 10 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        ()  
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (10,0), False, (10,10), 100, 200)
        print("-->Test 11 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,10), False, (10,10), 100, 200)
        print("-->Test 12 : ArgsException should occurre, location is outside the maze")
        succes = False
    except ArgsException as e:
        ()         

    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,0), 0, (10,10), 100, 200)
        print("-->Test 13 : ArgsException should occurre, randomStart is not a boolean")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        PlayerFactory.createPlayer(1010, "AIs/RatTest.py", (0,0), False, (10,10), 100, 200)
        print("-->Test 14 : ArgsException should occurre, animal is not a string")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        PlayerFactory.createPlayer("rat", 5658, (0,0), False, (10,10), 100, 200)
        print("-->Test 15 : ArgsException should occurre, file is not a string")
        succes = False
    except ArgsException as e:
        ()
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,10), False, 200)
        print("-->Test 16 : ArgsException should occurre, preparationTime is not a int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,10), -100, 200)
        print("-->Test 17 : ArgsException should occurre, preparationTime is not negative")
        succes = False
    except ArgsException as e:
        ()         
             
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,10), 100, "hello")
        print("-->Test 18 : ArgsException should occurre, turnTime is not a int")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (0,0), False, (10,10), 100, -200)
        print("-->Test 19 : ArgsException should occurre, turnTime is not negative")
        succes = False
    except ArgsException as e:
        () 
        
    try:
        AiPlayer = PlayerFactory.createPlayer("rat", "AIs/RatTest.py", (1,1), False, (10,10), 100, 200)
        dummyPlayer = PlayerFactory.createPlayer("rat", "InexistantFile", (2,2), False, (10,10), 100, 200)
        humanPlayer = PlayerFactory.createPlayer("rat", "human", (3,3), False, (10,10), 100, 200)
        inactivePlayer = PlayerFactory.createPlayer("rat", "", (4,4), False, (10,10), 100, 200)
    except ArgsException as e:
        print("-->Test 20 : ArgsException occurred, but should not")
        success = False
        
    if type(AiPlayer) != AIPlayer:
        print("-->Test 21 : AiPlayer is not a type of AIPlayer. Received : " + type(AiPlayer))
        success = False     
    if type(dummyPlayer) != AIPlayer:
        print("-->Test 22 : DummyPlayer is not a type of AIPlayer. Received : " + type(dummyPlayer))
        success = False  
    if type(humanPlayer) != HumanPlayer:
        print("-->Test 23 : humanPlayer is not a type of HumanPlayer. Received : " + type(humanPlayer))
        success = False         
    if type(inactivePlayer) != InactivePlayer:
        print("-->Test 24 : inactivePlayer is not a type of InactivePlayer. Received : " + type(inactivePlayer))
        success = False 
        
    if not(AiPlayer.plays()):
        print("-->Test 25 : AiPlayer does not play but it should")
        success = False     
    if not(dummyPlayer.plays()):
        print("-->Test 26 : DummyPlayer does not play but it should")
        success = False  
    if not(humanPlayer.plays()):
        print("-->Test 27 : humanPlayer does not play but it should")
        success = False         
    if inactivePlayer.plays():
        print("-->Test 28 : inactivePlayer does not play but it should")
        success = False     
                     
    return succes    
    



def giveResult(test):
    if test:
        print("----SUCCES")
    else:
        print("----FAILURE")
    
def main():
    PlayerTests()
    AIPlayerTests()
    HumanPlayerTests()
    InactivePlayerTests()
    giveResult(PlayerFactoryTests())
    
if __name__ == "__main__":
    main()
    