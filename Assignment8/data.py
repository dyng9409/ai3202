#data structure
#each State object holds
#State name as a string
#Count that keeps track of the number of times it appears
#a dict for the transition model
#a dict for the emissions model
#maintain normal count, smooth based on length of dict
class State(object):

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.transitions = {}
        self.emissions = {}
        statestring = 'abcdefghijklmnopqrstuvwxyz'
        for elt in list(statestring):
            self.transitions[elt] = 1
        if name == '_':
            #can only emit space
            self.emissions['_'] = 1
            #can only transition to [a-z]
        elif name == 'dummy':
            #can only emit dummy state
            self.emissions['dummy'] = 2
            #can only transition to [a-z]
            self.count = 1
        else:
            #can emit [a-z]
            #can transition to [a-z_] or EOF
            for elt in list(statestring):
                self.emissions[elt] = 1
            self.transitions['_'] = 1

    def getEmitProb(self, emit):
        #get emission probability of emit
        emitCount = self.emissions[emit]
        outcomeCount = len(self.emissions)
        denom = float(outcomeCount+self.count)
        return emitCount/denom

    def getTransProb(self, trans):
        #get transition probability of trans
        transCount = self.transitions[trans]
        outcomeCount = len(self.transitions)
        denom = float(outcomeCount+self.count)
        return transCount/denom

    def updateEmit(self, emit):
        #update count of emitted emit
        self.emissions[emit] += 1
        return

    def updateTrans(self, trans):
        #update count of emitted trans
        self.transitions[trans] += 1
        return

    def updateCount(self):
        #update state count
        self.count += 1
        return

    def printEmissions(self):
        #prints emissions CPT
        print 'Emissions CPT for state ', self.name
        for key, val in self.emissions.iteritems():
            print key+' | '+str(self.getEmitProb(key))
        return

    def printTransitions(self):
        #print transitions CPT
        print 'Transition CPT for state ', self.name
        for key, val in self.transitions.iteritems():
            print key+' | '+str(self.getTransProb(key))
        return

#spaces seem to always be transcribed properly, and dont ever seem to be
#erroneously inserted
#if this is the case, output space for transition model is 1 extra (27)

#so, if spaces CAN be erroneously inserted (but not replaced):
#emission space: [a-z_] for all except '_' which is always '_'
#transition space: [a-z_] for all
#emission normalization: count + 27, except for '_'
#transition norm: count+27

#if not, then emission space is only [a-z], norm = count+26, '_' is '_'
#tran space: [a-z_] norm = count+27, except '_' space=[a-z], norm = count+26

#data
states = {}
statestring = 'abcdefghijklmnopqrstuvwxyz_'
states['dummy'] = State('dummy')
for elt in list(statestring):
    states[elt] = State(elt)
