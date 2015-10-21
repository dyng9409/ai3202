#data structure for bayes nets

class Node(object):
    
    def __init__(self, name):
        #conditional and priors set to None for easy root
        #and leaf/intermediate checking
        #name is string
        self.name = name
        #dict of conditional probabilities
        self.cond = None
        #list of parent nodes
        self.parents = None
        #list of parent nodes
        self.children = None
        #prior probabilities (mutually exclusive with cond)
        self.prior = None

    def getName(self):
        return self.name

    def getChildren(self):
        return self.children

    def getParents(self):
        return self.parents

    def getCond(self):
        return self.cond

    def getPrior(self):
        return self.prior

    def setPrior(self, val):
        self.prior = val
        return


class Net(object):

    def __init__(self):
        self.nodeDict = {}

    def addNode(self, node):
        nodename = node.getName()
        self.nodeDict[nodename] = node

    def jointProbability(self, events):
        print 'calculating joint probability for'
        print events
        return
    
    def condProbability(self, events1, events2):
        print 'calculating conditional probability for'
        print events1
        print 'and'
        print events2
        return

    def marginalProbability(self, events):
        print 'calculating marginal probability for'
        print events
        return

    def getNode(self, nodeName):
        return self.nodeDict[nodeName]
