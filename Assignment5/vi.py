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

    if maxU == leftEU:
        return (reward+gamma*leftEU, 'left')
    elif maxU == rightEU:
        return (reward+gamma*rightEU, 'right')
    elif maxU == upEU:
        return (reward+gamma*upEU, 'up')
    else:
        return (reward+gamma*downEU, 'down')

    
def valueIteration(worldmap, epsilon):
    gamma = 0.9
    start = worldmap.get(0,0)
    pass
