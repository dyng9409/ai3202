import mapParse
import argparse
import vi
import world

parser = argparse.ArgumentParser()
parser.add_argument('worldfile', nargs=1, help='name of world textfile')
parser.add_argument('eps', type=float, nargs=1, help='choice of heuristic. 1 is manhattan distance, 2 is *')

args = parser.parse_args()

eps = args.eps[0]
worldsource = args.worldfile[0]

wmap = mapParse.parse(worldsource)

vi.valueIteration(wmap, eps)
start = wmap.get(0,0)
goal = wmap.get(wmap.xbound, wmap.ybound)
utility = 0
curNode = start

while curNode.typ is not 'goal':
    curU = curNode.utility
    utility = utility + curU
    curx = curNode.x
    cury = curNode.y
    if curx==0 and cury==0:
        print (curx, cury), ' START'
    else:
        print(curx, cury), 'Current Utility: ',round(utility,3)
    nextmove = curNode.optimal
    if nextmove is 'left':
        curNode = wmap.get(curx-1, cury)
    elif nextmove is 'right':
        curNode = wmap.get(curx+1, cury)
    elif nextmove is 'up':
        curNode = wmap.get(curx,cury+1)
    else:
        curNode = wmap.get(curx,cury-1)
print (curNode.x, curNode.y),' FINISH'
utility = curNode.utility + utility
print 'Final Utility: ', round(utility,3)
