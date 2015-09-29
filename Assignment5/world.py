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
        self.delta = float('inf')
        self.utility = 0
        self.reward = r

    def getReward(self):
        return self.reward

    def getUtility(self):
        return self.utility

    def setUtility(self, val):
        self.utility = val

    def getOptimal(self):
        return self.optimal

    def setOptimal(self, val):
        self.optimal = val

    def getDelta(self):
        return self.delta

    def setDelta(self, val):
        self.delta = val

    def getTyp(self):
        return self.typ
    
    def getx(self):
        return self.x

    def gety(self):
        return self.y

class Map(object):

    def __init__(self,lst):
        #lst should be a 2-dimensional rectangular array
        #(i.e. list of lists)
        self.map = lst
        self.ybound = len(lst)-1
        if self.ybound >= 0:
            self.xbound = len(lst[0])-1
        else:
            self.xbound < 0

    def get(self,x,y):
        #returns the node at coordinates x,y
        if x > self.xbound or x < 0:
            return None
        elif y > self.ybound or y < 0:
            return None
        elif self.map[y][x].typ == 'wall':
            return None
        else:
            return self.map[y][x]

    def printOptimal(self):
        for y in range(self.ybound,-1,-1):
            for x in range(0, self.xbound+1):
                if self.get(x,y) is not None:
                    print (self.get(x,y).optimal, round(self.get(x,y).utility,3)),
                else:
                    print 'wall',
            print '\n'


