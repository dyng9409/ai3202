import mapParse
import argparse
import heapq

parser = argparse.ArgumentParser()
parser.add_argument('worldfile', nargs=1, help='name of world textfile')
parser.add_argument('heuristic', type=int, nargs=1, help='choice of heuristic. 1 is manhattan distance, 2 is *')

args = parser.parse_args()

heur = args.heuristic[0]
worldsource = args.worldfile[0]

wmap = mapParse.parse(worldsource)

if heur == 1:
    wmap.applyHeuristic1()
else:
    wmap.applyHeuristic2()

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

    if node.xval() == xbound:
        if node.yval() == 0:
            #this is the goal node...
            return []
        elif node.yval() == ybound:
            for y in range(-1,1):
                for x in range(-1,1):
                    if x == 0 and y == 0:
                        continue
                    else:
                        retlist.append(worldMap.get(node.xval()+x, node.yval()+y))

    
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

    while not oplist:
        #TODO
        current = heapq.heappop(oplist)
        heapq.heapify(oplist)
        explored += 1

        curx = current.xval()
        cury = current.yval()
        #get adjacent squares

    return 

astarsearch(wmap)
