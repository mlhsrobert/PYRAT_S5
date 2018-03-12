import random
from core.parameters import *


class MazeInfo:
    
    
    def __init__(self,width, height, maze, piecesOfcheese):
        self.__width = width
        self.__height = height
        self.__maze = maze
        self.__piecesOfCheese = piecesOfcheese
        self.__initialNbPiecesCheese = len(piecesOfcheese)
            
    def getMaze(self):
        return self.__maze
        
    def getMazeSize(self):
        return (self.__width, self.__height)
    
    def getInitialNbPiecesCheese(self):
        return self.__initialNbPiecesCheese
    
    def getPiecesOfCheese(self):
        return self.__piecesOfCheese
    
    def removeAPieceOfCheese(self, location):
        self.__piecesOfCheese.remove(location)