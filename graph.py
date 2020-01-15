# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 00:54:43 2020

@author: dell
"""

from nlppreprocess import NLP
import pandas as pd
from sklearn.externals import joblib
import pandas as np
import pickle
import sklearn.feature_extraction
import numpy as np
import nltk
from sklearn.metrics import confusion_matrix


from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

df = pd.read_excel('Book1.xlsx')
#df.head()


df.dropna(inplace=True)


empty = []

"""for i,lb,rv in df.itertuples():
    if type(rv)==str:
        if rv.isspace():
            empty.append(i)
            
            
df.drop(empty, inplace=True)"""

sid.polarity_scores(df.loc[0]['SentimentText'])


df['scores'] = df['SentimentText'].apply(lambda review: sid.polarity_scores(review))
#df.head()


df['compound'] = df['scores'].apply(lambda score_dict: score_dict['compound'])
#df.head()



df['comp_score'] = df['compound'].apply(lambda c: 'pos' if c>=0 else 'neg')
#df.head()
c=0 #neg
d=0 # positive
k=df['comp_score']
p=list(k)
o=len(p)
for i in p:
    if i=='neg':
        c=c+1
    else:
        d=d+1
c=(c/o)*100
d=(d/o)*100

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Positive','Negative')
y_pos = np.arange(len(objects))
performance = [d,c]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('% of people')
plt.title('sentiment')

plt.show()