import argparse
import re
import data

parser = argparse.ArgumentParser(description = 'Calculator for Bayes Net Probabilities')
parser.add_argument('-p', nargs='+', help = 'Update prior for Smoking')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-j', metavar='Joint', nargs='+', help='Gives joint probability')
group.add_argument('-m', metavar='Marginal', nargs='+', help='Gives marginal probability')
group.add_argument('-g', metavar='Conditional', nargs='+', help='Gives conditional probability')
parser.set_defaults(p=None, j=None, m=None, g=None)

args = parser.parse_args()
priorArgs = args.p
bnet = data.bnet
#for now, we're going to assume the argument to p is nice formatted and blah blah blah

#setting the priors if its flagged
if priorArgs is not None:
    setval = float(priorArgs[1])
    if priorArgs[0] == 'S':
        editNode = bnet.getNode('smoking')
        editNode.setPrior(setval)
    else:
        editNode = bnet.getNode('pollution')
        editNode.setPrior(setval)
events = None
#finding which probability we're returning
if args.j is not None:
    bnet.jointProbability(args.j)
    events = args.j
    pass
#pipe has to be in quotes for this to work?
elif args.g is not None:
    splitargs = list(args.g[0])
    splitdex = splitargs.index('|')
    target = splitargs[0:splitdex]
    conditions = splitargs[splitdex+1:]
    retvals = bnet.condProbability(target, conditions)
    events = args.g
    pass
else:
    eventlist = data.net.subArgs(list(args.m[0]), bnet)
    (desc, retvals) = bnet.marginalProbability(eventlist)
    params = args.m[0]
    event = eventlist[0]
    print 'In the case of pollution, True corresponds to Low'
    if re.search("[PSCXD]", params) is not None:
        print desc
        print retvals
    elif re.search('~', params) is not None:
        print desc + ' False'
        print retvals[event.false]
    else:
        print desc + ' True'
        print retvals[event.true]

#should have functions return distributions, and then pick from there what
#is asked for
