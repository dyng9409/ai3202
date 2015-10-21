#data structure for bayes nets
import re

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

    def marginalProbability(self, event):
        print 'calculating marginal probability for'
        print event
        target = None
        event = event[0] 
        if re.search('d|D', event) is not None:
            target = self.getNode('dys')
        elif re.search('x|X', event) is not None:
            target = self.getNode('xray')
        elif re.search('p|P', event) is not None:
            target = self.getNode('pollution')
        elif re.search('c|C', event) is not None:
            target = self.getNode('cancer')
        elif re.search('s|S', event) is not None:
            target = self.getNode('smoking')
        else:
            print 'uwotm8'
            return {}

        if target.getName() == 'pollution':
            priorLow = target.getPrior()
            priorHigh = float('{0:.2f}'.format(1-priorLow))
            if event == 'P':
                retdict = {
                        'L':priorLow,
                        'H':priorHigh
                        }
            elif event == 'p':
                retdict = {
                        'L':priorLow
                        }
            else:
                retdict = {
                        'H':priorHigh
                        }
        elif target.getName() == 'smoking':
            priorTrue = target.getPrior()
            priorFalse = 1-priorTrue
            if event == 'S':
                retdict = {
                        'T':priorTrue,
                        'F':priorFalse
                        }
            elif event == 's':
                retdict = {
                        'T':priorTrue
                        }
            else:
                retdict = {
                        'F':priorFalse
                        }
        elif target.getName() == 'cancer':
            spriorTrue = self.getNode('smoking').getPrior()
            spriorFalse = float('{0:.2f}'.format(1-spriorTrue))
            ppriorTrue = self.getNode('pollution').getPrior()
            ppriorFalse = float('{0:.2f}'.format(1-ppriorTrue))
            cond = target.getCond()
            cancerMarginal = 0
            cancerMarginal += cond['HT']*spriorTrue*ppriorFalse
            cancerMarginal += cond['HF']*spriorFalse*ppriorFalse
            cancerMarginal += cond['LT']*spriorTrue*ppriorTrue
            cancerMarginal += cond['LF']*spriorFalse*ppriorTrue
            cancerMarginalF = 1-cancerMarginal
            if event == 'C':
                retdict = {
                        'T':cancerMarginal,
                        'F':cancerMarginalF
                        }
            elif event == 'c':
                retdict = {
                        'T':cancerMarginal
                        }
            else:
                retdict = {
                        'F':cancerMarginalF
                        }
        else:
            cancerprob = self.marginalProbability('C')
            cancerTrue = cancerprob['T']
            cancerFalse = cancerprob['F']
            cond = target.getCond()
            marginal = 0
            marginal += cond['T']*cancerTrue
            marginal += cond['F']*cancerFalse
            marginalFalse = 1-marginal
            if event == 'X' or event == 'D':
                retdict = {
                        'T':marginal,
                        'F':marginalFalse
                        }
            elif event == 'x' or event == 'd':
                retdict = {
                        'T':marginal
                        }
            else:
                retdict = {
                        'F':marginalFalse
                        }

        return retdict

    def getNode(self, nodeName):
        return self.nodeDict[nodeName]
