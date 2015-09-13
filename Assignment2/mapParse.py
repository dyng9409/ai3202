#parse the map file
import world

def parse(f):
    #parses the map file and returns a 
    #graph object containing the data

    data = open(f,'r')

    #read in all the lines
    preSq = data.readlines()
    data.close()

    sq = []
    for line in preSq:
        sq.append(line.split())

    #remove any blank lines
    while sq.count([]) > 0:
        sq.remove([])

    #now we're left with a list of lists with the main
    #property of each square
    
    #turn each element into a Node object with more descriptive data
    for y in range(0,len(sq)):
        for x in range(0,len(sq[0])):
            sq[y][x] = world.Node(sq[y][x],x,y)


    #finally, creating a mroe concrete map object for us to work with
    worldmap = world.Map(sq)

    return worldmap

def applyHeuristic1(world):
    #applying our chosen heuristic
    xbound = world.xbound
    ybound = world.ybound

    for y in range(0,ybound):
        for x in range(0,xbound):
            n = world.get(x,y)
            heur = (xbound-x-1)+(ybound-y-1)
            n.setHeuristic(heur)

def applyHeuristic2(world):
    #TODO
    xbound = world.xbound
    ybound = world.ybound

    for y in range(0,ybound):
        for x in range(0,xbound):
            n = world.get(x,y)
            heur = 0
            n.setHeuristic(heur)
