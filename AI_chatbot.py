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

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings) + '.'

#create index sort function descending,max at first index and other ascending
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index

#Create the bot response
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten() #flatten the list
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0 #if we found 2 or less smilar sentences, we will use top 2
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            response_flag = 1
            bot_response = bot_response + sentence_list[index[i]]
            j = j + 1
        if j >= 2:
            break
    if response_flag == 0 and user_input.lower() in ['sadge', 'sadgebot', 'why','why not', 'understand me',':('] :
        bot_response = bot_response +':('
    elif response_flag == 0: #if there is no similar sentence
        bot_response = bot_response + 'I am sorry, I am still a machine in the end of the universe'


    sentence_list.remove(user_input)
    return bot_response

#Start the chat
print('Hi, I am Philosopher Chatbot. I can answer your questions about belief.If you want to exit, type bye!')

exit_list = ['bye', 'exit', 'quit', 'goodbye', 'see you later','break']

while True:
    user_input = input()
    if user_input.lower() in exit_list:
        print('Bye!')
        break
    else:
        if greeting_response(user_input) != None:
            print('Philosopher Chatbot :', greeting_response(user_input))
        else:
            print('Philosopher Chatbot :', bot_response(user_input))