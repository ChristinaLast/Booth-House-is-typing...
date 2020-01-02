#modified from:
#https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
from sklearn.manifold import TSNE
import csv
import time

print("start", time.strftime("%H:%M:%S"))

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = [unicode(word) for word in get_stop_words('en')]

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
   
lookup = {}
doc_set = [] 
# create sample documents
with open('output_redo_noPunc.csv') as f:    
    reader = csv.reader(f, delimiter=",")
    c = 0
    for row in reader:
        lookup[c] = row[0]
        doc_set.append(unicode(row[1].lower(), errors='replace'))
        c = c + 1

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    stemmed_tokens = []
    for w in stopped_tokens:
      try:
          stemmed_tokens.append(unicode(p_stemmer.stem(w)))
      except UnicodeDecodeError:
          stemmed_tokens.append(w)
    
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

print("corpus", time.strftime("%H:%M:%S"))

numTopics=10
# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel.load("tmp031417/lda-noPunc"+str(numTopics)+"topics100")

print("loaded", time.strftime("%H:%M:%S"))

with open("tmp031417/lda-noPunc"+str(numTopics)+"topicBook100.csv", "wb") as f:
    writer = csv.writer(f)
    for j in xrange(len(lookup)):
        t = ldamodel.get_document_topics(corpus[j])
        topics  = [list(i) for i in t]
        topics_flat = [item for sublist in topics for item in sublist]
        temp = [j, lookup[j]] + topics_flat# + [doc_set[j]]
        writer.writerow(temp)
        
print("written", time.strftime("%H:%M:%S"))
