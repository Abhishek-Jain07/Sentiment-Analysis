# -*- coding: utf-8 -*-

#Data processing packages
import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', 200)

#Visualization packages
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import  WordCloud
from wordcloud import STOPWORDS

#NLP packages
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import nltk
nltk.download('movie_reviews')
nltk.download('punkt')

import warnings
warnings.filterwarnings("ignore")

#Testing NLP - Sentiment Analysis using TextBlob
y=TextBlob("The Product is good", ).sentiment
#Testing NLP - Sentiment Analysis using NaiveBayes
x=TextBlob("The Product is very very good", analyzer=NaiveBayesAnalyzer()).sentiment
print(y)
print(x)

#Importing Amazon comments data
comm = pd.read_csv('/Reviews.csv',encoding='utf8',error_bad_lines=False)#opening the file 

comm

#Displaying the first 5 rows of the data
data.head()

#Finding the size of the data
data.shape

#Extracting 1000 random samples from the data
comm = data.sample(2000)
comm.shape

#Calculating the Sentiment Polarity
pol=[] # list which will contain the polarity of the comments
for i in comm.reviews.values:
    try:
        analysis =TextBlob(i)
        pol.append(analysis.sentiment.polarity)
        
    except:
        pol.append(0)

#Adding the Sentiment Polarity column to the data
comm['pol']=pol

#Converting the polarity values from continuous to categorical
comm['pol'][comm.pol==0]= 0
comm['pol'][comm.pol > 0]= 1
comm['pol'][comm.pol < 0]= -1

#Displaying the POSITIVE comments
df_positive = comm[comm.pol==1]
df_positive.head(10)

#Displaying the NEGATIVE comments
df_positive = comm[comm.pol==-1]
df_positive.head(10)

#Displaying the NEUTRAL comments
df_positive = comm[comm.pol==0]
df_positive.head(10)

comm.pol.value_counts().plot.bar()
comm.pol.value_counts()

df = pd.read_csv('/Reviews.csv',encoding='utf8',error_bad_lines=False);
comment_words = ' '
stopwords = set(STOPWORDS)

# iterate through the csv file 
for val in df.reviews: 
      
    # typecaste each val to string 
    val = str(val) 
  
    # split the value 
    tokens = val.split() 
      
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
          
    
    comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words)

# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()