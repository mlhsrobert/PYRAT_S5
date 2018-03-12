MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

def locationsToMove (location1, location2) :
    
    # Depends on the difference
    difference = (location2[0] - location1[0], location2[1] - location1[1])
    if difference == (-1, 0) :
        return MOVE_LEFT
    elif difference == (1, 0) :
        return MOVE_RIGHT
    elif difference == (0, 1) :
        return MOVE_UP
    elif difference == (0, -1) :
        return MOVE_DOWN
    else :
        return 'None'

####################################################################################################################################################################################################################################
# Breadth first search algorithm to compute the shortest paths from the initial locations to all the nodes #
# Returns for each location the previous one that leads to the shortest path                               #
############################################################################################################

def breadthFirstSearch (mazeMap, initialLocation) :
    
    # We initialize the queue with the source node
    # Distances and routes are updated once the nodes are visited
    queue = [initialLocation]
    distances = {initialLocation:0}
    routes = {initialLocation:None}
    
    # Main loop
    while len(queue) != 0 :
        
        # We remove the head of the list
        location = queue[0]
        del queue[0]
        
        # We check the non-visited neighbors
        for neighbor in mazeMap[location] :
            if neighbor not in distances :
                distances[neighbor] = distances[location] + 1
                routes[neighbor] = location
                queue.append(neighbor)
    
    # Result
    return (routes, distances)
    
####################################################################################################################################################################################################################################
# Takes as an input the result of the search algorithm        #
# Returns the sequence of nodes from sourceNode to targetNode #
###############################################################

def routesToPath (routes, targetNode) :
    
    # Recursive reconstruction
    if targetNode in routes :
        return routesToPath(routes, routes[targetNode]) + [targetNode]
    else :
        return []   

####################################################################################################################################################################################################################################
# Returns the sequence of moves in the maze associated to a path in the graph #
###############################################################################

def pathToMoves (path) :
    
    # Recursive reconstruction
    if len(path) <= 1 :
        return []
    else :
        return [locationsToMove(path[0], path[1])] + pathToMoves(path[1:])
    
def shortestPathWithoutMud(mazeMap, startLocation, targetLocation):
    (routes, distances) = breadthFirstSearch(mazeMap, startLocation)

    shortestPath = routesToPath(routes, targetLocation)
    return shortestPath

