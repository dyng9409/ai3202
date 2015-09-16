#implementation of node and
#graph data strcuture for
#a* search

class Node(object):
    
    def __init__(self,t,x,y):
        self.typ = t
        self.x = x
        self.y = y
        self.distanceToStart = 0
        self.heuristic = 0
        self.f = 0
        self.parent = None

    def xval(self):
        return self.x

    def yval(self):
        return self.y

    def fval(self):
        return self.f

    def distVal(self):
        return self.distanceToStart

    def hval(self):
        return self.heuristic

    def setF(self, val):
        self.f = val

    def setParent(self,p):
        self.parent = p

    def setDistance(self,val):
        self.distanceToStart = val

    def setHeuristic(self,val):
        self.heuristic = val

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

    def applyHeuristic1(self):
        for y in range(0,self.ybound):
            for x in range(0,self.xbound):
                n = self.get(x,y)
                heur = ((self.xbound-x-1)+(self.ybound-y-1))*10
                n.setHeuristic(heur)

    def applyHeuristic2(self):
        limval = 0
        if self.ybound > self.xbound:
            limval = self.ybound-1
        else:
            limval = self.xbound-1
        for y in range(0,self.ybound):
            for x in range(0,self.xbound):
                n = self.get(x,y)
                #TODO: new heuristic
                selfx = n.xval()
                selfy = n.yval()
                sumcoord = x+y
                heur = 0
                if sumcoord == limval:
                    heur = 14*selfy
                elif sumcoord < limval:
                    heur = 14*selfy+10*(self.xbound-(selfx+selfy)-1)
                else:
                    heur = 14*(self.xbound-selfx-1)+10*(selfy-(self.xbound-selfx-1))

                n.setHeuristic(heur)

