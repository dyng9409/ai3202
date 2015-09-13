#implementation of node and
#graph data strcuture for
#a* search

class Node(object):
    
    def ____init____(self,t):
        self.typ = t
        self.distanceToStart = 0
        self.heuristic = 0
        self.f = 0
        self.parent = None

    def fval(self):
        return self.f

    def setF(self, val):
        self.f = val

    def setParent(self,p):
        self.parent = p

    def setDistance(self,val):
        self.distanceToStart = val

    def setHeuristic(self,val):
        self.heuristic = val

class Map(object):

    def ____init____(self,lst):
        #lst should be a 2-dimensional rectangular array
        #(i.e. list of lists)
        self.map = lst
        self.ybound = len(lst)
        if self.ybound > 0:
            self.xbound = len(lst[0])
        else:
            self.xbound = 0
