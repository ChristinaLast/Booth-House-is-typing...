import gensim
import csv
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import gc
import time

print ("start", time.strftime("%H:%M:%S"))

with open('./tmp031417/output_redo_noPunc.csv', 'rb') as f:
    reader = csv.reader(f)
    inputArray = list(reader)

sentences = []
for item in inputArray:
  sentences.append(item[1].split())
'''
with open('output_redo_noPunc.csv', 'rb') as f:
    reader = csv.reader(f)
    inputArray = list(reader)

sentences = []
print(len(inputArray))
for item in inputArray:
  c = 0;
  sub = ""
  for j in item:
    if c > 1:
      j = j.split()
      for q in j:
        sub = sub + " " + ''.join(e for e in q if e.isalnum()).lower()
    c = c+1
  sentences.append(str(sub.strip()))
  
with open("./tmp031417/output_redo_noPunc.csv", "wb") as f:
    writer = csv.writer(f)
    for i in xrange(len(sentences)):
      writer.writerow([inputArray[i][1],sentences[i]])
'''
print ("data collected", time.strftime("%H:%M:%S"))



model = gensim.models.Word2Vec(sentences,
				size=300, 
				window=2, 
				min_count=1, 
				workers=1)   
				                      
model.intersect_word2vec_format('../vectorProcessing/GoogleNews-vectors-negative300.bin', lockf=1.0, binary=True)  

count = 2

for i in xrange(count): 
    model.train(sentences)

items = model.wv.vocab.items()
X = model[model.wv.vocab]

del model

print ("model created", time.strftime("%H:%M:%S"))

tsne = TSNE(n_components=3)
X_tsne = tsne.fit_transform(X)

print (X_tsne.shape)

print ("tsne complete", time.strftime("%H:%M:%S"))

with open("./tmp031417/mymodel_trained_noPunc_repeat"+str(count)+".csv", "wb") as f:
    writer = csv.writer(f)
    for i in xrange(X_tsne.shape[0]):
        temp = X_tsne[i, :].tolist()
        temp.append(items[i][0])
        writer.writerow(temp)
        
print ("csv written", time.strftime("%H:%M:%S"))
