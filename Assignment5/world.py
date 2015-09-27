#implementation of node and
#graph data strcuture for
#a* search
#revised for MDP VI

class Node(object):
    
    def __init__(self,t,x,y):
        self.typ = t
        self.x = x
        self.y = y
        self.distanceToStart = 0
        self.heuristic = 0
        self.f = 0
        self.parent = None


class Map(object):

    def __init__(self,lst):
        #lst should be a 2-dimensional rectangular array
        #(i.e. list of lists)
        self.map = lst
        self.ybound = len(lst)
        if self.ybound > 0:
            self.xbound = len(lst[0])
        else:
            self.xbound = 0

    def get(self,x,y):
        #returns the node at coordinates x,y
        return self.map[y][x]
