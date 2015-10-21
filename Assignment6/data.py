import net


bnet = net.Net()

smokingNode = net.Node('smoking')
pollutionNode = net.Node('pollution')
cancerNode = net.Node('cancer')
xrayNode = net.Node('xray')
dysNode = net.Node('dys')


smokingNode.prior = 0.3
smokingNode.children = [cancerNode]
pollutionNode.prior = 0.9
smokingNode.children = [cancerNode]

cancerNode.cond = {
                    'HT': 0.05,
                    'HF': 0.02,
                    'LT': 0.03,
                    'LF': 0.001
                  }
cancerNode.parents = [pollutionNode, smokingNode]
cancerNode.children = [xrayNode, dysNode]
#key is string with random variable value
#H = high polution, L = low pollution
#T = smokes, F = not smokes
#example key: HF (high polution and doesn't smoke)
#value will be decimal between 0 and 1 as usual
#represents POSITIVE (e.g. probability that cancer occurs given HF)
#for nodes with multiple parents, the variables are in the order that the 
#parent list is (so for cancer, the parent list is POLLUTION

xrayNode.cond = {
                  'T': 0.9,
                  'F': 0.2
                }
xrayNode.parents = [cancerNode]

dysNode.cond = {
                 'T': 0.65,
                 'F': 0.30
               }
dysNode.parents = [cancerNode]

bnet.addNode(smokingNode)
bnet.addNode(pollutionNode)
bnet.addNode(cancerNode)
bnet.addNode(xrayNode)
bnet.addNode(dysNode)
