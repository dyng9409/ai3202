import argparse
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

#finding which probability we're returning
if args.j is not None:
    bnet.jointProbability(args.j)
    pass
#pipe has to be in quotes for this to work?
elif args.g is not None:
    bnet.condProbability(args.g, args.g)
    pass
else:
    retvals = bnet.marginalProbability(args.m)
    pass

#should have functions return distributions, and then pick from there what
#is asked for

print retvals
