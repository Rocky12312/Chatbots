#The basics steps in preprocessing and cleaning textual data:
#As our model input can be only numerical data so here our task will be to convert out textual data to numerical data,so that it can be fed to our model
#So for example let's say we are creating our document taking data in form of html documents


import os
import sys
import urllib
import itertools
import tarfile
# Download data to current working directory 
url = "url to our data"
#Making directory where we will basically store our data
if not os.path.exists("data directory"):
    os.mkdir("data directory name")
urllib.request.urlretrieve(url, "path to directory where we store our data")
# uncompressing the data(say we have a zip file)
compressed = zipfile.open("path to data file downloaded")
compressed.extractall(path = "directory where to store data")
compressed.close()
# List the uncompressed data
os.listdir("listing the files in directory") 

#Now usually the next step will be to add this data(it depends on us how much we require)to a list
#As we will be having a folder in which we have data so we need to iterate to append it
txt_list = []
#n is no of files we require
for i in range(n):
    filename = "path to the file+name"
    f = open(filename,"r",errors = "ignore"):
    txt_list.append(f.read())


#So as our data might contains tags(in html format if taken from web source)
#So now removing tags from our data(if we have normal text no need of this step)
import re
import string
from bs4 import BeautifulSoup 
#Now as our txt_list elements might be containing large no of tags so better split it into smaller  articles.
txt_article = []
for textfile in txt_list:
    #Parsing the text as html using beautiful soup
    prsd_text = BeautifulSoup(textfile, 'html.parser')
    #Extracting all the txt source between the body tags
    txt_article = txt_article + [article.get_text() for article in prsd_text.find_all('body')]
#Checking the first txt_article
print(txt_article[0])

import nltk
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download("stopwords")
nltk.download("wordnet")
from collections import defaultdict
#Now as majorly we will be having the plain text(free of tags) in our txt_article now removing all the punctuations the numeric characters(Keeping only the text articles)
txt_article = [article.lower() for article in txt_article]
#Strip all punctuation from each article
remove_punct = dict((ord(punct), None) for punct in string.punctuation)
txt_article = [article.translate(remove_punct) for article in txt_article]
#Removing all the numerics from the text(or can also replace the numerics with string num)
txt_article = [re.sub(r'\[[0-9]*\]', '', article) for article in txt_article]
txt_article = [re.sub(r'\s+', '', article) for article in txt_article]
#Removing all the stopwords from the text(words which appear most frequently like the,in etc)
txt_article = [[word for word in article.split() if word not in set(stopwords.words("english"))] for article in txt_article]
#Now using either stemmer of lemmatizer to reduce the words to its root form(basically stemmer stems the word while on the other hand lemmatizer reduce the word to its root form)
#Basically we use pos tagging before lemmatizing(use pos tagging will be a better option)
lemmatizer = WordNetLemmatizer()
txt_article = [" ".join([lemmatizer.lemmatize(word) for word in article]) for article in txt_article]

#Now as basically we have preprocessed and cleaned our text(next we can vectorize our text making it ready to be used in a model)

#Using Tfidf Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
#n is number of the words we want in our feature vector
tfidf = TfidfVectorizer(max_feature = n)
tfidf = tfidf.fit_transform(txt_article)
#Now we will get a matrix of article vs features

#Or using Count vectorizer(bag of words model)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = n)
cv = cv.fit_transform(txt_article)
#We will get a count matrix

#Tfidf is a better choice then count vectorizer(but again it depends on the problem statement)
#These are the steps taken in text preprocessing and cleaning(may be we can some more preprocessing but again it depends on the problem)
