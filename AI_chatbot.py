#pip install nltk
#pip install newspaper3k
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

#Tokenize the article (split the article into sentences)
text = corpus
sentence_list = nltk.sent_tokenize(text) #convert to list of sentences

#Print the sentence list
print(sentence_list)

# A function to return a random greeting response
def greeting_response(text):
    text = text.lower()
    # Bot Responses
    bot_greetings = ['hi', 'hello', 'hey', 'hola', 'greetings', 'sup', 'what\'s up', 'hey there', 'hey', 'hi there', 'hello there', 'hey there', 'howdy', 'how are you', 'how\'s it going', 'how\'s it going?']

    # User Greetings
    user_greetings = ['hi', 'hello', 'hey', 'hola', 'greetings', 'sup', 'what\'s up', 'hey there', 'hey', 'hi there', 'hello there', 'hey there', 'howdy', 'how are you', 'how\'s it going', 'how\'s it going?']

    for word in text.splot():
        if word in user_greetings:
            return random.choice(bot_greetings) + '.'
            