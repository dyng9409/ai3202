#parse the map file
import map as m

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

    return sq
