TEAM_NAME = "Barbe Rouge"

MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

import random
import time

count = 0
moves = ['None','None','None','None','None','None','None','None','None','None','D','L','L','U','L','L','L','D','R','D','R','R','R','L','D','L','D','D','U','L','U','D','L','U','L','L','R','R','D','D','D','D','R','R','L','L','U','L','L','D','L','D','L','U','U','U','L','U','U','D','D','R','U','R','L','U','D','D','L','D','U','R','D','D','D','R','R','R','D','R','D','L','L','L','U','L','R','D','R','R','R','R','U','R','R','L','L']

def preprocessing(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese, timeAllowed):
    if mazeWidth <= 0 or mazeHeight <= 0:
        print("Erreur preprocessing : dimension maze incorrecte")
    if playerLocation[0]<0 or playerLocation[1]<0:
        print("Erreur preprocessing : playerLocation incorrecte")
    if opponentLocation[0]<0 or opponentLocation[1]<0:
        print("Erreur preprocessing : playerLocation incorrecte")
    if timeAllowed <0:
        print("Erreur preprocessing : timeAllowed incorrect")
    return

def postprocessing (mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, 
                    playerScore, opponentScore, piecesOfCheese, timeAllowed):
    if mazeWidth <= 0 or mazeHeight <= 0:
        print("Erreur postprocessing : dimension maze incorrecte")
    if playerLocation[0]<0 or playerLocation[1]<0:
        print("Erreur postprocessing : playerLocation incorrecte")
    if opponentLocation[0]<0 or opponentLocation[1]<0:
        print("Erreur postprocessing : playerLocation incorrecte")
    if timeAllowed <0:
        print("Erreur postprocessing : timeAllowed incorrect")    
    if playerScore <0 :
        print("Erreur postprocessing : playerScore incorrect") 
    if opponentScore <0 :
        print("Erreur postprocessing : opponentScore incorrect")    
    return

def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed): 
    if mazeWidth <= 0 or mazeHeight <= 0:
        print("Erreur turn : dimension maze incorrecte")
    if playerLocation[0]<0 or playerLocation[1]<0:
        print("Erreur turn : playerLocation incorrecte")
    if opponentLocation[0]<0 or opponentLocation[1]<0:
        print("Erreur turn : playerLocation incorrecte")
    if timeAllowed <0:
        print("Erreur turn : timeAllowed incorrect")    
    if playerScore <0 :
        print("Erreur turn : playerScore incorrect") 
    if opponentScore <0 :
        print("Erreur turn : opponentScore incorrect")     
    
    global count
    global moves
    move = "None"
    try:
        move = moves[count]
        count +=1
    except:
        count +=1
    return move
    
