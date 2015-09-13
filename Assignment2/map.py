#implementation of node and
#graph data strcuture for
#a* search

class Node(object):
    
    def ___init___(locx,locy,heur):
        self.location = (locx,locy)
        self.distanceToStart = 0
        self.heuristic = heur
        self.f = 0
        self.parent = None
