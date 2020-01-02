import csv
from collections import Counter
import math

with open('./tmp031417/lookupTable.csv', 'rb') as f:
    reader = csv.reader(f)
    inputArray = list(reader)
    
count = 0
newList = []
for item in inputArray:
  i = map(int, item)
  i = sorted(i)
  newList.append(' '.join([str(x) for x in i]))
  
q = dict(Counter(newList))

with open("./tmp031417/lookupTable-circles.csv", "wb") as f:
    writer = csv.writer(f)
    for i in newList:
        temp = [math.log(q[i])] + i.split()
        writer.writerow(temp)
