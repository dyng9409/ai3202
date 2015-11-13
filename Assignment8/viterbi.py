import CPTgen
from math import log

states = CPTgen.data.states
f = open('typos20Test.data')

#opening period
f.readline()

#timed data
paths = [{}]
truestring = ''
#initialize from dummy state
firstLine = f.readline()
firstEvidence = firstLine[2]
truestring = truestring+firstLine[0]
#for all the things that dummy can transition to
dstate = states['dummy']
for firstState in dstate.transitions:
    fstate = states[firstState]
    try:
        emitProbability = fstate.getEmitProb(firstEvidence)
        transitionProbability = dstate.getTransProb(firstState)
        belief = log(emitProbability) + log(transitionProbability)
        paths[0][firstState] = (belief, 'dummy')
    except:
        continue

#now to go through the file
curTime = 0
for line in f:
    curTime += 1
    paths.append({})
    newEvidence = line[2]
    truestring += line[0]
    for newState in states:
        possibleTransitions = []
        try:
            emitProbability = states[newState].getEmitProb(newEvidence)
        except:
            continue 
        for previousState in paths[curTime-1]:
            pState = states[previousState]
            try:
                transitionProbability = pState.getTransProb(newState)
            except:
                continue 
            (prevBelief, parent) = paths[curTime-1][previousState]
            belief = log(transitionProbability)+log(emitProbability)+prevBelief
            possibleTransitions.append((belief, previousState))
        paths[curTime][newState] = max(possibleTransitions)

paths.reverse()
maxt = (float("-inf"), '')
maxs = ''
for key, val in paths[0].iteritems():
    if val[0] > maxt[0]:
        maxt = val
        maxs = key

outputstr = maxs
pathsiter = iter(paths)
next(pathsiter)
for elt in pathsiter:
    #maxt = ('', float("-inf"))
    #maxs = ''
    parent = maxt[1]
    maxt = elt[parent]
    outputstr = parent+outputstr
    #for key, val in elt.iteritems():
    #    if  val[1] > maxt[1]:
    #        maxt = val
    #        maxs = key
    #outputstr = maxs+outputstr

print outputstr
errcount = 0
for index in range(0, len(outputstr)):
    if outputstr[index] != truestring[index]:
        errcount +=1
print '\n---------------------\n'
print 'Error rate: %', 100*float(errcount)/len(outputstr)
