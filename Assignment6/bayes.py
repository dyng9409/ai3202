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
    eventlist = data.net.subArgs(list(args.j[0]), bnet)
    (desc, retvals) = bnet.jointProbability(eventlist)
    params = args.j[0]
    print desc
    if re.search("[PSCXD]", params) is not None:
        if re.search("~", params) is not None:
            if params[0] is '~':
                for key,val in retvals.iteritems():
                    if key[0] is False and key[1] is True:
                        print key, val
                    elif key[0] is False and key[1] is False:
                        print key, val
            else:
                for key, val in retvals.iteritems():
                    if key[0] is True and key[1] is False: 
                        print key, val
                    elif key[0] is False and key[1] is False:
                        print key, val
        elif re.search("[pscxd]", params) is not None:
            if re.search("[pscxd]", params[0]) is not None:
                for key, val in retvals.iteritems():
                    if key[0] is True and key[1] is True:
                        print key, val
                    elif key[0] is True and key[1] is False:
                        print key, val
            else:
                for key, val in retvals.iteritems():
                    if key[0] is True and key[1] is True:
                        print key, val
                    elif key[0] is False and key[1] is True:
                        print key, val
        else:
            print retvals
    elif re.search('~', params) is not None:
        if params[0] is '~':
            if params[2] is '~':
                print retvals[False, False]
            else:
                print retvals[False, True]
        else:
            print retvals[True, False]
    else:
        print retvals[True, True]
#pipe has to be in quotes for this to work?
elif args.g is not None:
    splitargs = list(args.g[0])
    splitdex = splitargs.index('|')
    target = splitargs[0:splitdex]
    conditions = splitargs[splitdex+1:]
    ev0 = data.net.subArgs(target, bnet)
    ev1 = data.net.subArgs(conditions, bnet)
    (desc, retvals) = bnet.condProbability(ev0[0], ev1)
    print desc
    if re.search("[PSCXD]", target[0]) is not None:
        if re.search("[PSCXD]", conditions[0]) is not None:
            print retvals
        elif re.search("~", conditions[0]) is not None:
            for key, val in retvals.iteritems():
                if key[1] is False:
                    print key, retvals[key]
        else:
            for key, val in retvals.iteritems():
                if key[1] is True:
                    print key, retvals[key]
    elif re.search("~", target[0]) is not None:
        if re.search("[PSCXD]", conditions[0]) is not None:
            for key, val in retvals.iteritems():
                if key[0] is False:
                    print key,retvals[key]
        elif re.search("~", conditions[0]) is not None:
            for key, val in retvals.iteritems():
                if key[0] is False and key[1] is False:
                    print key, retvals[key]
        else:
            for key, val in retvals.iteritems():
                if key[0] is False and key[1] is True:
                    print key, retvals[key]
    else:
        if re.search("[PSCXD]", conditions[0]) is not None:
            for key, val in retvals.iteritems():
                if key[0] is True:
                    print key,retvals[key]
        elif re.search("~", conditions[0]) is not None:
            for key, val in retvals.iteritems():
                if key[0] is True and key[1] is False:
                    print key, retvals[key]
        else:
            for key, val in retvals.iteritems():
                if key[0] is True and key[1] is True:
                    print key, retvals[key]
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

