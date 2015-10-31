import re
import random

class Node(object):

    def __init__(self, name):
        self.name = name
        self.prior = None
        self.CPT = None

f = open('data.txt')
final = ''
for line in f:
    x = re.sub('\n', '', line)
    x = re.sub('\[', '', x)
    x = re.sub('\]', '', x)
    final = final+' '+x
f.close()
final = final.split()
samples = []
for elt in final:
    x = re.sub(',','',elt)
    x = float(x)
    samples.append(x)

cloudy = Node('cloudy')
sprinklers = Node('sprinklers')
rain = Node('rain')
wetgrass = Node('wetgrass')

cloudy.prior = 0.5
sprinklers.CPT = {
        True:0.1,
        False:0.5
        }
rain.CPT = {
        True:0.8,
        False:0.2
        }
wetgrass.CPT = {
        (True, True):0.99,
        (True, False):0.9,
        (False, True):0.9,
        (False, False):0.0
        }
#sampling order: c -> s -> r -> w
#generate all samples:
sampleList = []
sampleIndex = 0
while sampleIndex < len(samples):
    insertDict = {}
    if samples[sampleIndex] <= cloudy.prior:
        #cloudy is true
        insertDict['c'] = True
    else:
        insertDict['c'] = False
    sampleIndex += 1
    cval = insertDict['c']
    if samples[sampleIndex] <= sprinklers.CPT[cval]:
        insertDict['s'] = True
    else:
        insertDict['s'] = False
    sampleIndex += 1
    if samples[sampleIndex] <= rain.CPT[cval]:
        insertDict['r'] = True
    else:
        insertDict['r'] = False
    sampleIndex += 1
    sval = insertDict['s']
    rval = insertDict['r']
    if samples[sampleIndex] <= wetgrass.CPT[sval, rval]:
        insertDict['w'] = True
    else:
        insertDict['w'] = False
    sampleIndex += 1
    sampleList.append(insertDict)
print '-----PRIOR SAMPLING-----'
sampleSize = len(sampleList)
cloudyCount = 0
#p(c)
for elt in sampleList:
    if elt['c'] is True:
        cloudyCount += 1
print 'Total samples: ', sampleSize
print 'Total cloudy days: ', cloudyCount
print 'P(c = true): ', cloudyCount/float(sampleSize)
print '\n'

#p(c|r)
rainyCount = 0
raincloudCount = 0
for elt in sampleList:
    if elt['r'] is True:
        rainyCount += 1
        if elt['c'] is True:
            raincloudCount += 1

print 'Total rainy days: ', rainyCount
print 'Total cloudy on rainy days: ', raincloudCount
print 'P(c = true | r = true): ', raincloudCount/float(rainyCount)
print '\n'

wetCount = 0
sprwetCount = 0
for elt in sampleList:
    if elt['w'] is True:
        wetCount += 1
        if elt['s'] is True:
            sprwetCount += 1

print 'Total wet grass days: ', wetCount
print 'Total sprinklers on wet grass days: ', sprwetCount
print 'P(s = true | w = true): ', sprwetCount/float(wetCount)
print '\n'

cwCount = 0
sCount = 0
for elt in sampleList:
    if elt['c'] is True:
        if elt['w'] is True:
            cwCount += 1
            if elt['s'] is True:
                sCount += 1

print 'Total Cloudy and Wet Grass days: ', cwCount
print 'Total sprinklers on those days: ', sCount
print 'P(s = true | c = true, w = true): ', sCount/float(cwCount)
print '\n'

print '-----REJECTION SAMPLING-----'
cloudCount = 0
for val in samples:
    if val <= cloudy.prior:
        cloudCount += 1
print 'Total Cloudy days: ', cloudCount
print 'Total days: ', 100
print 'P(c = true): ', cloudCount/100.0
print '\n'

ind = 0
sampleList = []
while True:
    if ind >= 99:
        break
    insertDict = {}
    sampleVal = samples[ind]
    if sampleVal <= cloudy.prior:
        insertDict['c'] = True
    else:
        insertDict['c'] = False
    ind += 1
    sampleVal = samples[ind]
    if sampleVal <= rain.CPT[insertDict['c']]:
        insertDict['r'] = True
        sampleList.append(insertDict)
    else:
        insertDict['r'] = False
    ind += 1

cloudC = 0

for elt in sampleList:
    if elt['c'] is True:
        cloudC += 1

print 'Total rainy days: ', len(sampleList)
print 'Total cloudy days on rainy days: ', cloudC
print 'P(c = true | r = true): ', cloudC/float(len(sampleList))
print '\n'

ind = 0
sampleList = []
while True:
    if ind >= 96:
        break
    insertDict = {}
    sampleVal = samples[ind]
    if sampleVal <= cloudy.prior:
        insertDict['c'] = True
    else:
        insertDict['c'] = False
    cval = insertDict['c']
    ind += 1
    sampleVal = samples[ind]
    if sampleVal <= sprinklers.CPT[cval]:
        insertDict['s'] = True
    else:
        insertDict['s'] = False
    sval = insertDict['s']
    ind += 1
    sampleVal = samples[ind]
    if sampleVal <= rain.CPT[cval]:
        insertDict['r'] = True
    else:
        insertDict['r'] = False
    rval = insertDict['r']
    ind += 1
    if not sval and not rval:
        continue
    sampleVal = samples[ind]
    if sampleVal <= wetgrass.CPT[sval, rval]:
        insertDict['w'] = True
        sampleList.append(insertDict)
    ind += 1

scount = 0
for elt in sampleList:
    if elt['s'] is True:
        scount += 1

print 'Total wet grass days: ', len(sampleList)
print 'Total sprinklers on wet grass days: ', scount
print 'P(s = true | w = true): ', scount/float(len(sampleList))
print '\n'

ind = 0
sampleList = []
while True:
    if ind >= 96:
        break
    insertDict = {}
    sampleVal = samples[ind]
    if sampleVal <= cloudy.prior:
        insertDict['c'] = True
    else:
        ind += 1
        continue
    ind += 1
    sampleVal = samples[ind]
    if sampleVal <= sprinklers.CPT[True]:
        insertDict['s'] = True
    else:
        insertDict['s'] = False
    sval = insertDict['s']
    ind += 1
    sampleVal = samples[ind]
    if sampleVal <= rain.CPT[True]:
        insertDict['r'] = True
    else:
        insertDict['r'] = False
    rval = insertDict['r']
    ind += 1
    if not sval and not rval:
        continue
    sampleVal = samples[ind]
    if sampleVal <= wetgrass.CPT[sval, rval]:
        insertDict['w'] = True
        sampleList.append(insertDict)
    ind += 1

scount = 0
for elt in sampleList:
    if elt['s'] is True:
        scount += 1

print 'Total number of cloudy and wet grass days: ', len(sampleList)
print 'Total number of sprinklers on during those days: ', scount
print 'P(s = true | c = true, w = true): ', scount/float(len(sampleList))
