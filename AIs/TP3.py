import heapq
    
####################################################################################################################################################################################################################################
# Dijkstra's algorithm to compute the shortest paths from the initial locations to all the nodes #
# Returns for each location the previous one that leads to the shortest path                     #
##################################################################################################

def dijkstra (mazeMap, initialLocation) :
    
    # We initialize the min-heap with the source node
    # Distances and routes are updated once the nodes are visited for the first time
    # The temporary values are stored in the min-heap
    minHeap = [(0, initialLocation, None)]
    distances = {}
    routes = {}
    
    # Main loop
    while len(minHeap) != 0 :
        (distance, location, predecessor) = heapq.heappop(minHeap)
        if location not in distances :
            distances[location] = distance
            routes[location] = predecessor
            for neighbor in mazeMap[location] :
                newDistanceToNeighbor = distance + mazeMap[location][neighbor]
                heapq.heappush(minHeap, (newDistanceToNeighbor, neighbor, location))
    
    # Result
    return (routes, distances)

def routesToPath (routes, targetNode) :
    
    # Recursive reconstruction
    if targetNode in routes :
        return routesToPath(routes, routes[targetNode]) + [targetNode]
    else :
        return [] 
    
def shortestPathWithMud(mazeMap, startLocation, targetLocation):
    (routes, distances) = dijkstra(mazeMap, startLocation)

    shortestPath = routesToPath(routes, targetLocation)
    return shortestPath