import re

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

#prior sampling, p(c)
