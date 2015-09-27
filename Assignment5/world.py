#implementation of node and
#graph data strcuture for
#a* search
#revised for MDP VI

class Node(object):
    
    def __init__(self,t,x,y,r):
        self.typ = t
        self.x = x
        self.y = y
        self.optimal = None
        self.delta = 0
        self.utility = 0
        self.reward = r 

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
