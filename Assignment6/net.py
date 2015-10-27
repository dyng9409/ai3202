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
        if len(events) is 2:
            ev0 = events[0]
            ev1 = events[1]
            ev0p = events[0].getParents()
            ev1p = events[1].getParents()
            ev0c = self.nodeDict[ev0]
            ev1c = self.nodeDict[ev1]
            if ev0p is None and ev1p is None:
                retdict = {
                        (ev0.true, ev1.true):ev0.prior*ev1.prior,
                        (ev0.true, ev1.false):ev0.prior*(1-ev1.prior),
                        (ev0.false, ev1.true):(1-ev0.prior)*ev1.prior,
                        (ev0.false, ev1.false):(1-ev0.prior)*(1-ev1.prior)
                        }
                desc = "Variable order: " + ev0.getName() + ', '+ev1.getName()
                return (desc, retdict)
            elif len(ev0c) is 0 and len(ev1c) is 0:
                ev0prob = self.marginalProbability([ev0])[1][True]
                ev1prob = self.marginalProbability([ev1])[1][True]
                retdict = {
                        (ev0.true, ev1.true):ev0prob*ev1prob,
                        (ev0.true, ev1.false):ev0prob*(1-ev1prob),
                        (ev0.false, ev1.true):(1-ev0prob)*ev1prob,
                        (ev0.false, ev1.false):(1-ev0prob)*(1-ev1prob)
                        }
                desc = "Variable order: "+ev0.getName()+', '+ev1.getName()
                return (desc, retdict)
            else:
                #otherwise, we're going to need onditional dependency
                (desc, retvals) = self.condProbability(ev0, [ev1])
                prob = self.marginalProbability([ev1])[1][True]
                for key, val in retvals.iteritems():
                    if key[1] is True:
                        retvals[key] = val*prob
                    else:
                        retvals[key] = val*(1-prob)
                desc = ev0.name+' '+ev1.name
                return (desc, retvals)
        else:
            return
    
    def condProbability(self, event0, events1):
        #conditional probability for 1 and 1
        if len(events1) is 1:
            ev1 = events1[0]
            ev1p = ev1.getParents()
            if ev1p is None:
                ev1p = []
            ev0 = event0
            ev0p = ev0.getParents()
            if ev0p is None:
                ev0p = []
            if ev1 in ev0p:
                ev1prob = self.marginalProbability([ev1])[1][True]
                ev0prob = ev0.getCond()
                #given T and given F
                ev0probT = 0 
                ev0probF = 0
                if ev0.name is 'cancer':
                    if ev1.name is 'pollution':
                        sprob = self.getNode('smoking').prior
                        pprob = self.getNode('pollution').prior
                        ev0probT = ev0prob[(True, True)]*sprob*pprob
                        ev0probT = ev0probT+ev0prob[(True, False)]*(1-sprob)*pprob
                        ev0probT = ev0probT/pprob
                        ev0probF = ev0prob[(False, True)]*sprob*(1-pprob)
                        ev0probF = ev0probF+ev0prob[(False, False)]*(1-sprob)*(1-pprob)
                        ev0probF = ev0probF/(1-pprob)

                    else:
                        sprob = self.getNode('smoking').prior
                        pprob = self.getNode('pollution').prior
                        ev0probT = ev0prob[(True, True)]*sprob*pprob
                        ev0probT = ev0probT+ev0prob[(False, True)]*(1-pprob)*sprob
                        ev0probT = ev0probT/sprob
                        ev0probF = ev0prob[(True, False)]*pprob*(1-sprob)
                        ev0probF = ev0probF+ev0prob[(False, False)]*(1-sprob)*(1-pprob)
                        ev0probF = ev0probF/(1-sprob)
                else:
                    ev0probT = ev0prob[True]
                    ev0probF = ev0prob[False]
                retdict = {
                        (ev0.true, ev1.true):ev0probT,
                        (ev0.true, ev1.false):ev0probF,
                        (ev0.false, ev1.true):1-ev0probT,
                        (ev0.false, ev1.false):1-ev0probF
                        }
                desc = 'Variable order: '+ev0.name+' given '+ev1.name
                return (desc, retdict)

            elif ev0 in ev1p:
                desc, rets = self.condProbability(ev1, [ev0])
                prob = self.marginalProbability([ev1])[1][True]
                prob2 = self.marginalProbability([ev0])[1][True]
                tmp = rets[(True, False)]
                rets[(True, False)] = rets[(False, True)]
                rets[(False, True)] = tmp
                for key, val in rets.iteritems():
                    if key[0] is True:
                        val = val*prob2
                    else:
                        val = val*(1-prob2)
                    if key[1] is True:
                        rets[key] = val/prob
                    else:
                        rets[key] = val/(1-prob)
                return desc, rets
            else:
                #case ev1 is ev0 ancestor
                if len(ev0p) is not 0:
                    cancerN = self.getNode('cancer')
                    pollN = self.getNode('pollution').prior
                    smokingN = self.getNode('smoking').prior
                    (desc, cancProb) = self.marginalProbability([ev0p[0]])
                    v1 = ev0.cond[True]
                    v2 = ev0.cond[False]
                    #v1(v3+v4)+v2(v5+v6)
                    v3 = cancerN.cond[True, True]*pollN*smokingN
                    v4 = 0
                    if ev1.name is 'smoking':
                        v4 = cancerN.cond[False, True]*(1-pollN)*smokingN
                    else:
                        v4 = cancerN.cond[True, False]*(1-smokingN)*pollN
                    v5 = (1-cancerN.cond[True, True])*pollN*smokingN
                    v6 = 0
                    if ev1.name is 'smoking':
                        v6 = (1-cancerN.cond[False, True])*(1-pollN)*smokingN
                    else:
                        v6 = (1-cancerN.cond[True, False])*(1-smokingN)*pollN
                    retdict = {}
                    retdict[True, True] = (v1*(v3+v4)+v2*(v5+v6))/(v3+v4+v5+v6)
                    retdict[False, True] = 1-retdict[True, True]

                    #v1(v3+v4)+v2(v5+v6)
                    v3 = cancerN.cond[False, False]*(1-pollN)*(1-smokingN)
                    v4 = 0
                    if ev1.name is 'smoking':
                        v4 = cancerN.cond[True, False]*(1-smokingN)*pollN
                    else:
                        v4 = cancerN.cond[False, True]*(1-pollN)*smokingN
                    v5 = (1-cancerN.cond[False, False])*(1-pollN)*(1-smokingN)
                    v6 = 0
                    if ev1.name is 'smoking':
                        v6 = (1-cancerN.cond[True, False])*(1-smokingN)*pollN
                    else:
                        v6 = (1-cancerN.cond[True, False])*(1-pollN)*smokingN

                    retdict[True, False] = (v1*(v3+v4)+v2*(v5+v6))/(v3+v4+v5+v6)
                    retdict[False, False] = 1-retdict[True, False]
                    desc = ev0.name+' '+ev1.name
                    return (desc, retdict)

                #case ev0 is ev1 ancesetor
                else:
                    (desc, rets) = self.condProbability(ev1, [ev0])
                    desc = ev0.name+' '+ev1.name
                    p = ev0.prior
                    (d, ret) = self.marginalProbability([ev1])
                    p2 = ret[True]
                    retdict = {}
                    retdict[True,True] = rets[True, True]*p/p2
                    retdict[True, False] = rets[False, True]*p/(1-p2)
                    retdict[False, True] =  1-retdict[True, True]
                    retdict[False, False] =  1-retdict[True, False]
                    return (desc, retdict)
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

