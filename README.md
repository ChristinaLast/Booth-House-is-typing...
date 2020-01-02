# Booth-House-is-typing...
Visualising Whatsapp data using word2vec mapping for the Booth House group chat “Guardian Angels” subjects in 3 dimensions, and graphing the content of each message in the resulting word cloud.

## Datasets
The messages subjects were analyzed using LDA from the gensim python library to create 10 topics:
![Gensim: LDA Model](https://radimrehurek.com/gensim/models/ldamodel.html)

The google news word vectors were used as a pregenerated Word2Vec model:
![Google News Word Vectors Description](https://code.google.com/archive/p/word2vec/) ![Google News Word Vectors Download](https://github.com/mmihaltz/word2vec-GoogleNews-vectors)

I retrained the google news word vectors with the book subjects using Gensim:
![Gensim: Word2Vec Model](https://radimrehurek.com/gensim/models/word2vec.html)

The resulting word vectors were brought down to three dimensions using t-SNE from the scikit learn python library:
![Scikit-Learn: t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)

### GIF of Visualisation

![]()

## Description:
Information privacy is the relationship between the collection and dissemination of data, technology, the public expectation of privacy, legal and political issues surrounding them. When private information makes its way into the eyes of the public, how do we interact with it?  

For this piece I downloaded the Whatsapp conversation data from “Guardian Angels” group chat. Because the conversation data did not have topics in the database I did topic modelling on the subjects to create my own "topics." I ran the word2vec analysis on the conversations topics. I then mapped the topic location and path based on the conversation data. Both the size and the darkness of the title dot represents how many conversation comments have the same topic vector.

## Interactivity:
Each LDA defined topic is given a separate colour which can be turned on and off. The conversations can be viewed in Title Mode, where the vectors can be turned on and off.
The word cloud can be used to see what conversations have topics that include the second word, the word topic information can be turned on and off.

When a point is hovered over the words/titles appear, the user can use the up and down arrow keys to cycle through the words/titles. The right and left arrow keys can be used to select a specific word/title and see the connections related to it.
