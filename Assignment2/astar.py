import search
import mapParse
import search
import mapParse
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('worldfile', nargs=1, help='name of world textfile')
parser.add_argument('heuristic', type=int, nargs=1, help='choice of heuristic. 1 is manhattan distance, 2 is *')

args = parser.parse_args()

heur = args.heuristic[0]
worldsource = args.worldfile[0]

wmap = mapParse.parse(worldsource)

if heur == 1:
    wmap.applyHeuristic1()
else:
    wmap.applyHeuristic2()

search.astarsearch(wmap)
