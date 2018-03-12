from util.errors import *
from player.AIPlayer import *
from player.HumanPlayer import *
from player.InactivePlayer import *

class PlayerFactory:
    
    def createPlayer(animal, file, location, randomStart, mazeSize, preparationTime, turnTime):
                
        if animal != "rat" and animal != "python":
            raise ArgsException("PlayerFactory.createPlayer : animal is incorrect") 
        
        if type(file) != str:
            raise ArgsException("PlayerFactory.createPlayer : file is not a string")         
        
        if type(mazeSize) != tuple:
            raise ArgsException("PlayerFactory.createPlayer : mazeSize is not a tuple")
        if type(mazeSize[0]) != int or type(mazeSize[1]) != int:
            raise ArgsException("PlayerFactory.createPlayer : mazeSize is not a tuple of int")  
        if mazeSize[0]<0 or mazeSize[1]<0 :
            raise ArgsException("PlayerFactory.createPlayer : mazeSize should not negative")               
        
        if type(location) != tuple:
            raise ArgsException("PlayerFactory.createPlayer : Location is not a tuple")
        if type(location[0]) != int or type(location[1]) != int:
            raise ArgsException("PlayerFactory.createPlayer : Location is not a tuple of int")
        if location[0]<0 or location[0]>=mazeSize[0] or location[1]<0 or location[1]>=mazeSize[1]:
            raise ArgsException("PlayerFactory.createPlayer : Location is not in the maze")
        
        if type(randomStart) != bool:
            raise ArgsException("PlayerFactory.createPlayer : randomStart is not a boolean")
        
        if type(preparationTime) != int:
            raise ArgsException("PlayerFactory.createPlayer : preparationTime is not a int")  
        if preparationTime < 0:
            raise ArgsException("PlayerFactory.createPlayer : preparationTime is negative") 
        
        if type(turnTime) != int:
            raise ArgsException("PlayerFactory.createPlayer : turnTime is not a int")  
        if turnTime < 0:
            raise ArgsException("PlayerFactory.createPlayer : turnTime is negative")           
            
        if file == "":
            return InactivePlayer(location, randomStart, mazeSize)
        elif file == "human" :
            return HumanPlayer(location, randomStart, mazeSize)
        else :
            return AIPlayer(animal, file, location, randomStart, mazeSize, preparationTime, turnTime)
        
        