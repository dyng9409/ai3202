import world

#bellman eq implementation
def updateUtility(worldmap, node, gamma):
    xcoord = node.getx()
    ycoord = node.gety()

    reward = node.getReward()
    selfU = node.getUtility()

    xlim = worldmap.xbound
    ylim = worldmap.ybound

    left = worldmap.get(xcoord-1, ycoord)
    right = worldmap.get(xcoord+1, ycoord)
    up = worldmap.get(xcoord, ycoord+1)
    down = worldmap.get(xcoord, ycoord-1)

    leftU = selfU
    rightU = selfU
    upU = selfU
    downU = selfU

    if left is not None:
        leftU = left.getUtility()

    if right is not None:
        rightU = right.getUtility()

    if up is not None:
        upU = up.getUtility()

    if down is not None:
        downU = down.getUtility()

    leftEU = 0.8*leftU + 0.1*downU +0.1*upU
    rightEU = 0.8*rightU + 0.1*downU + 0.1*upU
    upEU = 0.8*upU + 0.1*leftU + 0.1*rightU
    downEU = 0.8*downU + 0.1*leftU + 0.1*rightU

    maxEU = max(leftEU, rightEU, upEU, downEU)

    if maxEU == leftEU:
        return (reward+gamma*leftEU, 'left')
    elif maxEU == rightEU:
        return (reward+gamma*rightEU, 'right')
    elif maxEU == upEU:
        return (reward+gamma*upEU, 'up')
    else:
        return (reward+gamma*downEU, 'down')

    
def valueIteration(worldmap, epsilon):
    gamma = 0.9
    start = worldmap.get(0,0)
    goal = worldmap.get(worldmap.xbound, worldmap.ybound)
    goal.setUtility(50.0)

    deltaCutoff = epsilon*(1-gamma)/gamma
    changeFlag = True
    while changeFlag:
        changeFlag = False
        for x in range(worldmap.xbound,-1,-1):
            for y in range(worldmap.ybound,-1,-1):
                curNode = worldmap.get(x,y)
                if curNode is None:
                    continue
                elif curNode.typ is 'goal':
                    continue
                prevDelta = curNode.getDelta()
                curUtility = curNode.getUtility()
                if prevDelta < deltaCutoff:
                    continue
                else:
                    changeFlag = True
                    nextUtility = updateUtility(worldmap, curNode, gamma)
                    curNode.setUtility(nextUtility[0])
                    curNode.setOptimal(nextUtility[1])
                    diff = abs(curUtility-nextUtility[0])
                    if diff < prevDelta:
                        curNode.setDelta(diff)

