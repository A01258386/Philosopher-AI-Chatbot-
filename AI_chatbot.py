#Import the libraries
from newspaper import Article
import nltk
import string
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import numpy as np
warnings.filterwarnings('ignore')

#Download the punkt package
nltk.download('punkt')

#Get the article and assign it to a variable
article = Article('https://plato.stanford.edu/entries/belief/')
article.download()
article.parse()
article.nlp()
corpus = article.text

#Print the article
print(corpus)

#Tokenize the article
text = corpus
sentence_list = nltk.sent_tokenize(text) #convert to list of sentences
