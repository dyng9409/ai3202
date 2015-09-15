import heapq

def cost(src, dest):
    #will determine the cost (f value) of the square
    #i.e. cost to reach + heuristic
    #for simplicity, we will be assuming
    #the goal is always upper right
    
    
    return

def adj(worldMap, node):
    #will return a list of valid (non wall/existing) nodes
    retlist = []
    xbound = worldMap.xbound-1
    ybound = worldMap.ybound-1

    for x in range(-1,2):
        adjx = node.xval()+x
        if (adjx < 0) or (adjx > xbound):
            continue
        for y in range(-1,2):
            adjy = node.yval()+y
            if (adjy < 0) or (adjy > ybound):
                continue
            elif (y==0) and (x==0):
                continue
            else:
                adjnode = worldMap.get(adjx, adjy)
                if adjnode.typ != '2':
                    retlist.append(adjnode)
    
    return retlist

def astarsearch(worldMap):
    
    startx = 0
    starty = worldMap.ybound-1

    goalx = worldMap.xbound-1
    goaly = 0

    oplist = []
    closed = []
    explored = 0
    #node is considered explored when it is expanded
    cost = 0

    oplist.append(worldMap.get(startx, starty))
 
    while oplist:
        #TODO
        current = heapq.heappop(oplist)
        heapq.heapify(oplist)
        explored += 1

        curx = current.xval()
        cury = current.yval()
        #get adjacent squares
    return 


