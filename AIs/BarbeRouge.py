TEAM_NAME = "Barbe Rouge"
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

def aboveOf(position):
    return (position[0],position[1]+1)



def belowOf(position):
    return (position[0],position[1]-1)


def leftOf(position):
    return (position[0]-1,position[1])


def rightOf(position):
    return (position[0]+1,position[1])



def canMove(mazeMap,start,arrival):
    return arrival in mazeMap[start]


def getMove(mazeMap,start,arrival):
    if canMove(mazeMap,start,arrival)==False:
        return "None"
    else:
        if arrival[0]==start[0] and arrival[1]==start[1]+1:
            return 'U'


        elif arrival[0]==start[0] and arrival[1]==start[1]-1:
            return 'D'
        elif arrival[1]==start[1] and arrival[0]==start[0]+1:
            return 'R'
        else:
            return 'L'


###############################################################################
import heapq

def dijkstra(mazeMap,start):
    infini=10000                                                                # we fix the infinite at 10000
    priorityQueue=[]                                                            # creation of a priority queue
    heapq.heappush(priorityQueue,(start,0))                                     #we add the start, which has a distance of zero
    routing={i:0 for i in mazeMap}                                              # creation of the routing table as a dictionnary
    distances={i:infini for i in mazeMap}                                       # creation of table of distances, full of infinite because we didn't found a way to each node yet
    distances[start]=0                                                          # except the start (distance 0 from the start)

    while len(priorityQueue)!=0:                                                # while the queue is not empty ( we still have nodes to visit)                                                                         
        currentNode,distance=heapq.heappop(priorityQueue)                       # we remove the closest node from the queue                                                                                           
        for neighbor in mazeMap[currentNode]:                                   # for all its neihbors:
            distance2=distance+ mazeMap[currentNode][neighbor]                  # in a variable, we store the distance of the neigbor from the start
            if distances[neighbor] > distance2:                                 # if this new distance is shorter than the previous distance:
                distances[neighbor]=distance2                                   # we update                       
                heapq.heappush(priorityQueue,(neighbor,distance2))              # we had this neigbor with its distance at the queue 
                routing[neighbor]=currentNode                                   # we uptade the routing table


    return routing,distances


def shortestRoad(mazeMap,start,arrival):                                        # reconstitution of the shortest road to reach the arrival from the start                         
    road=[]                                                                     # creation of the list where we'll store the way to follow                                                                  
    currentNode=arrival                                                         # we start from the arrival and we go up to the start                   
    routing,distances=dijkstra(mazeMap,start)                                             # routing table thanks to the previous fonction                                     
    while currentNode != start:                                                 # we iterate until the start                        
        road.append(currentNode)                                                # we add in the list the node which adds the current node                     
        currentNode=routing[currentNode]                                        # so we place ourself on this node                            
    road.append(start)                                                          # finally we add the start ( because it is not added in the loop)                              

    return road                                                                 # the list stores the nodes in the reverse order ( from the arrival to the start)




def listOfMoves(mazeMap,start,arrival):                                         # function which returns the series of moves to do                                           
    road=shortestRoad(mazeMap,start,arrival)                                    # we use the previous fonction       
    movestodo=[]                                                                # list to store the moves to do 

    for i in range(len(road)-1,0,-1):                                           # iteration from the end of the road list(so the start) to the beginning (so the arrival)                       
        movestodo.append(getMove(mazeMap,road[i],road[i-1]))                    # we add the move to do thanks to the getmove function from the tp1          
    return movestodo




################################################################################

def newGraph(mazeMap,piecesOfCheese,start):
    listOfNodes=[start]+piecesOfCheese

    newMazeMap={k:{i:None for i in listOfNodes} for k in listOfNodes}
    for i in range (len(listOfNodes)-1):
        for j in range (i+1,len(listOfNodes)):
            routing,distances=dijkstra(mazeMap,listOfNodes[i])
            newMazeMap[listOfNodes[i]][listOfNodes[j]]=distances[listOfNodes[j]]
            newMazeMap[listOfNodes[j]][listOfNodes[i]]=distances[listOfNodes[j]]

    return newMazeMap


def heuristic(newMazeMap,piecesOfCheese,playerLocation):


    currentWeight=10000
    for neighbor in newMazeMap[playerLocation]:
        if neighbor in piecesOfCheese:
            if neighbor is not playerLocation:
                if newMazeMap[playerLocation][neighbor]<currentWeight:
                    nextNode=neighbor
                    currentWeight=newMazeMap[playerLocation][neighbor]


    return nextNode


def movement(newMazeMap,mazeMap,piecesOfCheese,playerLocation):
    node=heuristic(newMazeMap,piecesOfCheese,playerLocation)
    moves=listOfMoves(mazeMap,playerLocation,node)

    return moves


def preprocessing(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese,timeAllowed):      
    global moves
    global newMazeMap
    newMazeMap=newGraph(mazeMap,piecesOfCheese,playerLocation)
    moves=movement(newMazeMap,mazeMap,piecesOfCheese,playerLocation)


def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):   # at each move done, we removed it from the list to not do it again
    global moves
    if len(moves)==0:

        Moves=movement(newMazeMap,mazeMap,piecesOfCheese,playerLocation)
        move=Moves.pop(0)
        moves=Moves
    else:
        move=moves.pop(0)     
    return move

