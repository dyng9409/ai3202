import heapq

def adj(worldMap, node):
    #will return a list of valid (non wall/existing) nodes
    retlist = []
    xbound = worldMap.xbound-1
    ybound = worldMap.ybound-1

    for x in range(-1,2):
        adjx = node.xval()+x
        if (adjx < 0) or (adjx > xbound):
            continue
        for y in range(-1,2):
            adjy = node.yval()+y
            if (adjy < 0) or (adjy > ybound):
                continue
            elif (y==0) and (x==0):
                continue
            else:
                adjnode = worldMap.get(adjx, adjy)
                if adjnode.typ != '2':
                    retlist.append(adjnode)
    
    return retlist

def astarsearch(worldMap):
    
    startx = 0
    starty = worldMap.ybound-1

    goal = worldMap.get(worldMap.xbound-1,0)
    oplist = []
    closed = []
    explored = 0
    #node is considered explored when it is expanded
    cost = 0

    oplist.append((0, worldMap.get(startx, starty)))
 
    while oplist:
        current = heapq.heappop(oplist)[1]
        heapq.heapify(oplist)
        explored += 1

        curx = current.xval()
        cury = current.yval()
        curdistance = current.distVal()
        closed.append(current)
        if goal in closed:
            cost = goal.distVal()
            break
        #get adjacent squares
        adjacent = adj(worldMap, current)
        #examine each valid node, check if in closed or not
        for node in adjacent:
            if node in closed:
                continue
            nextx = node.xval()
            nexty = node.yval()
            if (node.fval(), node) in oplist:
                nextdist = node.distVal()
                if (curx-nextx == 0) or (cury - nexty == 0):
                    if node.typ == '0':
                        if (curdistance+10) < nextdist:
                            oplist.remove((node.fval(),node))
                            node.setParent(current)
                            node.setDistance(curdistance+10)
                            node.setF(node.distVal()+node.hval())
                            oplist.append((node.fval(),node))
                    else:
                        if (curdistance+20) < nextdist:
                            oplist.remove((node.fval(),node))
                            node.setParent(current)
                            node.setDistance(curdistance+20)
                            node.setF(node.distVal()+node.hval())
                            oplist.append((node.fval(),node))
                else:
                    if node.typ == '0':
                        if(curdistance+14) < nextdist:
                            oplist.remove((node.fval(),node))
                            node.setParent(current)
                            node.setDistance(curdistance+14)
                            node.setF(node.distVal()+node.hval())
                            oplist.append((node.fval(),node))
                    else:
                        if (curdistance+24) < nextdist:
                            oplist.remove((node.fval(),node))
                            node.setParent(current)
                            node.setDistance(curdistance+24)
                            node.setF(node.distVal()+node.hval())
                            oplist.append((node.fval(),node))
            else:
                #if it is to the left, right, up or down of the current square
                #and not in the current list
                node.setParent(current)
                if (curx-nextx == 0) or (cury - nexty == 0):
                    if node.typ == '0':
                        node.setDistance(curdistance+10)
                    else:
                        node.setDistance(curdistance+20)
                    fv = node.hval()+node.distVal()
                    node.setF(fv)
                    heapq.heappush(oplist, (fv, node))
                else:
                    if node.typ == '0':
                        node.setDistance(curdistance+14)
                    else:
                        node.setDistance(curdistance+24)
                    fv = node.hval() + node.distVal()
                    node.setF(fv)
                    heapq.heappush(oplist, (fv, node))

        heapq.heapify(oplist)

    print 'Path to goal:'
    print (goal.xval(),goal.yval()),'  END'
    n = goal.parent
    while n.parent is not None:
        print (n.xval(),n.yval())
        n = n.parent
    print (n.xval(), n.yval()),'  START'
    print 'Cost of path: ',cost
    print 'Squares explored: ',explored
    return 


