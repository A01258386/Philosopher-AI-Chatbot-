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