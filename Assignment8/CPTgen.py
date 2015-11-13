#parser for cpt generation
import data
#data structure requirements:
#dict-like
#key should be state
#value - another dict?
#{'b':{'a':emssioncount+1/statecount+27, 'b':emissioncount+1/statecount+27}}
#

#data.states holds all the states

f = open('typos20.data')
first = f.readline()
trueState = first[0]
evidence = first[2]
data.states['dummy'].updateTrans(trueState)
data.states[trueState].updateCount()
data.states[trueState].updateEmit(evidence)
for line in f:
    nextState = line[0]
    evidence = line[2]
    data.states[trueState].updateTrans(nextState)
    trueState = nextState
    data.states[trueState].updateCount()
    data.states[trueState].updateEmit(evidence)

statestring = 'abcdefghijklmnopqrstuvwxyz'
#getting rid of typos that never occur
for elt in list(statestring):
    deletelist = []
    for key, val in data.states[elt].emissions.iteritems():
        if val == 1:
            deletelist.append(key)
    for k in deletelist:
        del(data.states[elt].emissions[k])

#statestring = 'abcdefghijklmnopqrstuvwxyz_'
#data.states['dummy'].printTransitions()
#data.states['dummy'].printEmissions()
#print '\n----------\n'
#
#for elt in list(statestring):
#    data.states[elt].printTransitions()
#    print '\n----------\n'
#    data.states[elt].printEmissions()
#    print '\n----------\n'
