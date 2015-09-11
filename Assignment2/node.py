#implementation of node and
#graph data strcuture for
#a* search

class Node(object):
    
    def ___init___(self):
        self.location = (0,0)
        self.distanceToStart = 0
        self.heuristic = 0
        self.f = 0
        self.parent = None
