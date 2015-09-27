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
    sq.reverse()
    #now we're left with a list of lists with the main
    #property of each square
    #TODO maybe switch the y so its more intuivitve mapping 
    #turn each element into a Node object with more descriptive data
    for y in range(0,len(sq)):
        for x in range(0,len(sq[0])):
            if sq[y][x] == '0':
                sq[y][x] = world.Node('plain',x,y)
            elif sq[y][x] == '1':
                sq[y][x] = world.Node('mountain',x,y)
            elif sq[y][x] == '2':
                sq[y][x] = world.Node('wall',x,y)
            elif sq[y][x] == '3':
                sq[y][x] = world.Node('snake',x,y)
            elif sq[y][x] == '4':
                sq[y][x] = world.Node('barn',x,y)
            else:
                sq[y][x] = world.Node('goal',x,y)




    #finally, creating a mroe concrete map object for us to work with
    worldmap = world.Map(sq)

    return worldmap

