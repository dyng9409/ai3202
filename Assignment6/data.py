import net


bnet = net.Net()

smokingNode = net.Node('smoking')
pollutionNode = net.Node('pollution')
cancerNode = net.Node('cancer')
xrayNode = net.Node('xray')
dysNode = net.Node('dys')


smokingNode.prior = 0.3
pollutionNode.prior = 0.9

cancerNode.parents = [pollutionNode, smokingNode]
p = cancerNode.parents
cancerNode.cond = {
                    (p[0].false, p[1].true): 0.05,
                    (p[0].false, p[1].false): 0.02,
                    (p[0].true, p[1].true): 0.03,
                    (p[0].true, p[1].false): 0.001
                  }

xrayNode.parents = [cancerNode]
p = xrayNode.parents
xrayNode.cond = {
                  (p[0].true): 0.9,
                  (p[0].false): 0.2
                }

dysNode.parents = [cancerNode]
p = dysNode.parents
dysNode.cond = {
                 (p[0].true): 0.65,
                 (p[0].false): 0.30
               }

bnet.addNode(smokingNode, [cancerNode])
bnet.addNode(pollutionNode, [cancerNode])
bnet.addNode(cancerNode, [xrayNode, dysNode])
bnet.addNode(xrayNode, [])
bnet.addNode(dysNode, [])
