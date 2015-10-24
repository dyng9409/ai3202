#data structure for bayes nets
import re

def subArgs(symbols, nnet):
    #given a list of symbols, replace with appropriate events/nodes from net
    eventList = []
    for sym in symbols:
        if sym == 'c' or sym == 'C':
            eventList.append(nnet.getNode('cancer'))
        elif sym == 'd' or sym == 'D':
            eventList.append(nnet.getNode('dys'))
        elif sym == 's' or sym == 'S':
            eventList.append(nnet.getNode('smoking'))
        elif sym == 'p' or sym == 'P':
            eventList.append(nnet.getNode('pollution'))
        elif sym == 'x' or sym == 'X':
            eventList.append(nnet.getNode('xray'))
        else:
            continue
    return eventList
            
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
        #prior probabilities (mutually exclusive with cond)
        self.prior = None
        self.true = True
        self.false = False

    def getName(self):
        return self.name

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

    def addNode(self, node, dep):
        self.nodeDict[node] = dep

    def jointProbability(self, events):
        print 'calculating joint probability for'
        print events
        return
    
    def condProbability(self, event1, events2):
        print 'calculating conditional probability for'
        print event1
        print 'based on'
        print events2
        return

    def marginalProbability(self, event):
        target = event[0]
        if target.getParents() is None:
            retdict = {
                    target.true:target.getPrior(),
                    target.false:1-target.getPrior()
                    }
            desc = 'Variable Key Order: '+target.getName()
            return (desc,retdict)
        elif target.getName() is 'cancer':
            p0 = target.getParents()[0]
            p1 = target.getParents()[1]
            pcancer = 0
            for key, val in target.cond.iteritems():
                p0factor = p0.prior if key[0] is p0.true else 1-p0.prior
                p1factor = p1.prior if key[1] is p1.true else 1-p1.prior
                pcancer = pcancer + val*p0factor*p1factor
            retdict = {
                    target.true:pcancer,
                    target.false:1-pcancer
                    }
            desc = 'Variable Key Order: '+target.getName()
            return(desc, retdict)
        else:
            p0 = target.getParents()[0]
            ptarget = 0
            p0prior = self.marginalProbability([p0])[1][p0.true]
            for key, val in target.cond.iteritems():
                p0factor =  p0prior if key is p0.true else 1-p0prior
                ptarget = ptarget + val*p0factor

            retdict = {
                    target.true:ptarget,
                    target.false:1-ptarget
                    }
            desc = 'Variable Key Order: '+target.getName()
            return (desc, retdict)
        
    def getNode(self, nodeName):
        for key, val in self.nodeDict.iteritems():
            if key.getName() == nodeName:
                return key

