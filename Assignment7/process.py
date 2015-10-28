import re
f = open('data.txt')
final = ''
for line in f:
    x = re.sub('\n', '', line)
    x = re.sub('\[', '', x)
    x = re.sub('\]', '', x)
    final = final+' '+x
f.close()
final = final.split()
dataArray = []
for elt in final:
    x = re.sub(',','',elt)
    x = float(x)
    dataArray.append(x)
print len(dataArray)
