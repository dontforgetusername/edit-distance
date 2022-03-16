'''Code from example is maintained and the dimensionality reduction model is changed'''

import nltk
import gensim
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import pyplot

texts= [" Photography is an excellent hobby to pursue ",
        " Photographers usually develop patience, calmnesss"
        " You can try Photography with any good mobile too"]

# We prepare a list containing lists of tokens of each text
all_tokens=[]
for text in texts:
    tokens=[]
    raw=nltk.wordpunct_tokenize(text)
    for token in raw:
        tokens.append(token)
    all_tokens.append(tokens)

# Fit the model with data
model=Word2Vec(all_tokens, min_count=1)

# Visualize the word embedding
X = model.wv[list(model.wv.key_to_index)]
tsne = TSNE(n_components=2)
result = tsne.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(model.wv.key_to_index)
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()