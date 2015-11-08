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
print first
trueState = first[0]
evidence = first[2]
data.states['dummy'].updateTrans(trueState)
data.states[trueState].updateCount()
data.states[trueState].updateEmit(evidence)
for line in f:
    print line
    nextState = line[0]
    evidence = line[2]
    data.states[trueState].updateTrans(nextState)
    trueState = nextState
    data.states[trueState].updateCount()
    data.states[trueState].updateEmit(evidence)
