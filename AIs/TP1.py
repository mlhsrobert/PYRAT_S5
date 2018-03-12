
MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

def aboveOf(location):
    return (location[0], location[1]+1)

def belowOf(location):
    return (location[0], location[1]-1)

def leftOf(location):
    return(location[0]-1, location[1])

def rightOf(location):
    return(location[0]+1, location[1])

def canMove(mazeMap, fromLocation, toLocation):
    if fromLocation in mazeMap:
        possibilities = mazeMap.get(fromLocation)
        return toLocation in possibilities
    else:
        return False
    
def getMove(mazeMap, fromLocation, toLocation):
    if not canMove(mazeMap, fromLocation, toLocation):
        return "None"
    else:
        if fromLocation[0]-toLocation[0] == 1:
            return MOVE_LEFT
        elif fromLocation[0]-toLocation[0] == -1:
            return MOVE_RIGHT
        elif fromLocation[1]-toLocation[1] == 1:
            return MOVE_DOWN
        elif fromLocation[1]-toLocation[1] == -1:
            return MOVE_UP
        else :
            return "None"