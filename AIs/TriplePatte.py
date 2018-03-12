# AI for the game PyRat
# http://formations.telecom-bretagne.eu/pyrat

###############################
# Team name to be displayed in the game 
TEAM_NAME = "Triple-patte"

###############################
# When the player is performing a move, it actually sends a character to the main program
# The four possibilities are defined here
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

###############################
# Please put your imports here

import heapq

###############################
# Please put your global variables here

centerCheese = (0,0)
cheminDebut = []

###############################
# Preprocessing function
# The preprocessing function is called at the start of a game
# It can be used to perform intensive computations that can be
# used later to move the player in the maze.

# Arguments are:
# mazeMap : dict(pair(int, int), dict(pair(int, int), int))
# mazeWidth : int
# mazeHeight : int
# playerLocation : pair(int, int)
# opponentLocation : pair(int,int)
# piecesOfCheese : list(pair(int, int))
# timeAllowed : float

###############################
# This function is not expected to return anything
def preprocessing(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese, timeAllowed):
    global centerCheese
    global cheminDebut
    centerCheese=piecesOfCheese[0]

    cheminDebut=trouveChemin(dijkstra(mazeMap,playerLocation),playerLocation,centerCheese)

## Functions

def dijkstra(graph:dict, sourceNode:tuple) ->dict:    # Renvoie la table de routage correspondant à graph, en partant de sourceNode

    # Initialisation
    priorityQueue = [(sourceNode, 0)]       # Cette liste contiendra les cases que l'on sait qu'il nous reste à parcourir.
    distances={}                            # Ce dictionnaire contient les meilleurs distances trouvées entre sourceNode et toutes les autres cases
    for i in graph:                         # On commence par des longueurs infinies (problème d'optimisation)...
        distances[i]=float('inf')
    distances[sourceNode]=0                 # ...excepté pour sourceNode (on connaît déjà la distance sourceNode-sourceNode)
    routes = {}                             # Ce dictionnaire est la table de routage que l'on va remplir

    # Boucle
    while priorityQueue:                                                    # On s'arrête lorsqu'on a visité toutes les cases du labyrinthe
        currentNode, distance = heapq.heappop(priorityQueue)                # Pendant cette itération, on va travailler sur currentNode. On l'enlève de priorityQueue.
        for neighbor in graph[currentNode]:                                 # On visite tous les voisins de currentNode
            newDistance=distance+graph[currentNode][neighbor]               # Distance pour aller de sourceNode à neighbor en passant par currentNode
            if distances[neighbor] > newDistance:                           # Si la distance pour aller de sourceNode à neighbor normalement est plus longue...
                distances[neighbor] = newDistance                           # ...on met à jour les informations concernant neighbor
                heapq.heappush(priorityQueue, (neighbor, newDistance))
                routes[neighbor] = currentNode
    return routes

def trouveChemin(routes:dict, sourceNode:list, endNode:list) ->list:    # Renvoie la liste des cases à parcourir successivement pour aller de sourceNode à endNode. La première case est en dernier. 
    path=[]
    if sourceNode==endNode:                                             # Exception
        return path
    while endNode!=sourceNode:                                          # On remonte la table de routage en partant de endNode jusqu'à ce que l'on soit arrivé à sourceNode
        path.append(endNode)
        endNode=routes[endNode]
    return path

def above0f(position:tuple) -> tuple:       # Renvoie les coordonnées de la case située au dessus de la case dont les coordonnées ont été renseignées en entrée
    return (position[0],position[1]+1)

def below0f(position:tuple) -> tuple:       # Renvoie les coordonnées de la case située en dessous de la case dont les coordonnées ont été renseignées en entrée
    return (position[0],position[1]-1)

def left0f(position:tuple) -> tuple:        # Renvoie les coordonnées de la case située à gauche de la case dont les coordonnées ont été renseignées en entrée
    return (position[0]-1,position[1])

def right0f(position:tuple) -> tuple:       # Renvoie les coordonnées de la case située à droite de la case dont les coordonnées ont été renseignées en entrée
    return (position[0]+1,position[1])

def canMove(mazeMap:dict, fromLocation:tuple, toLocation:tuple) -> bool:    # Renvoie "True" ssi on peut se déplacer de fromLocation à toLocation en un déplacement
    return toLocation in mazeMap[fromLocation]

def getMove (mazeMap:dict, fromLocation:tuple, toLocation:tuple) ->str:  # Renvoie l'instruction à effectuer pour aller de fromLocation à toLocation, ou None si c'est impossible
    if canMove(mazeMap, fromLocation, toLocation):
        if above0f(fromLocation)==toLocation:           # Si toLocation est en haut de fromLocation, il faut aller en haut.
            return MOVE_UP
        if below0f(fromLocation)==toLocation:
            return MOVE_DOWN
        if left0f(fromLocation)==toLocation:
            return MOVE_LEFT
        return MOVE_RIGHT                               # Si l'on peut y aller, mais que ni le haut, ni le bas, ni la gauche fonctionne, c'est nécessairement la droite.
    return "None"

###############################
# Turn function
# The turn function is called each time the game is waiting
# for the player to make a decision (a move).

# Arguments are:
# mazeMap : dict(pair(int, int), dict(pair(int, int), int))
# mazeWidth : int
# mazeHeight : int
# playerLocation : pair(int, int)
# opponentLocation : pair(int, int)
# playerScore : float
# opponentScore : float
# piecesOfCheese : list(pair(int, int))
# timeAllowed : float

# This function is expected to return a move

def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):

    global cheminDebut

    if centerCheese in piecesOfCheese:
        return getMove(mazeMap, playerLocation, cheminDebut.pop())    

    routes=dijkstra(mazeMap, playerLocation)            # Première table de routage, construite à partir de playerLocation
    min_length=float('inf')                             # On commence par une longueur infinie (problème d'optimisation)

    for i in piecesOfCheese:                            # On cherche le fromage le plus proche parmi ceux restants
        chemin=trouveChemin(routes,playerLocation,i)    # On charge l'itinéraire vers le fromage sélectionné
        length=len(chemin)                              # On regarde sa longueur
        if length<min_length:                           # On compare au meilleur résultat pour l'instant
            min_length=length                           # Si on améliore la distance, on modifie la longueur de référence
            min_chemin=chemin                           # On sélectionne le nouveau plus court chemin
            fromage=i                                   # On sélectionne le nouveau fromage le plus près

    return getMove(mazeMap,playerLocation,min_chemin[-1])   # On commence à emprunter le chemin en aller à la dernière case du chemin qui est la prochaine étape


