#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os #as os
import data_object

from PIL import Image




from packages.graphical.generate_wordcloud import get_long_tweet_string


# In[ ]:


### Basic usage section

#print(op2)
#print(op2.shape)
#op2.head()
#print(op2.head())

                  
#op2['Text'].value_counts()
#op1[op2['Text'] == 'shit']

### Can be used to print all instead. Example parameters included
#with pd.option_context('display.max_rows', None):
#    print(op2)


# In[2]:


# Assign variables with examples
op1 = pd.read_csv('test.csv') 
op2 = pd.read_csv('trump.csv', usecols=['Name', 'Text'])
op3 = pd.read_csv('Ntrump.csv', usecols=['Name', 'Text', 'Place']


# In[30]:


### VISUALIZE
    ### Can be customized
    ### Stopwords can be commented / uncommented
    ### Weird bug (haven't figured) where top word will be printed as an empty spot if added to stopwords
from collections import Counter
Counter = Counter

sf = input("choose CSV to analyze")
file = open(sf, encoding="utf8")
a= file.read()# Stopwords
stopwords = set(line.strip() for line in open('stopwords.txt'))
stopwords = stopwords.union(set(['mr','mrs','one','two','said']))# Instantiate  dictionary if it doesn't exist. Else, count up
wordcount = {} # Eliminate duplicates

for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)# Close the file
file.close()# Create DF of most common words 
# VVV simple 'Bar chart'. To be continued
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')

#= collections.Counter 


# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:





# In[9]:


# Generate WordCloud
from os import path, getcwd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

##
file = input("Chose CSV\n")
filepath = open(file, encoding='utf8').read()
d = getcwd()
mask = np.array(Image.open(path.join(d, "mask.jpg")))

##
WC = WordCloud(background_color="black", max_words=40000, mask=mask, max_font_size=80, random_state=42)

#WC = WordCloud(width = 800, height = 800, 
 #               background_color ='blue',  
  #              min_font_size = 1)
WC.generate(filepath)

# plot WC                     
image_colors = ImageColorGenerator(mask)  
plt.figure(figsize = (15, 10)) 
plt.imshow(WC.recolor(color_func=image_colors), interpolation="bilinear") 
plt.axis("off")
plt.tight_layout(pad = 0) 
#WC.to_file("../wordcloud.png") 

plt.show() 


# In[ ]:





# In[ ]:





# In[8]:


### WordCloud. To be fixed

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def generate_wordcloud():
    WC = WordCloud(width = 800, height = 800, 
                   background_color ='white',  
                   min_font_size = 10).generate(word) 


    # plot WC                       
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(WC) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.show() 

generate_wordcloud()


# In[ ]:


sns.lmplot(x='Name', y='Text', data=op3)
 
# Alternative way
# sns.lmplot(x=df.Attack, y=df.Defense)


# In[27]:


list_words = ['Trump'.casefold(), 'anal','house']
filename = op3

# Tokenize
rm = ",:;?/-!."

# Read through the file per each line and do the math
with open(filename,'r') as fin:
    for count_line, line in enumerate(fin,1):
        clean_line = filter(lambda x: not (x in rm), line)
        # To hold the counts of each word
        words_frequency = {key: 0 for key in list_words}
        for w in clean_line.split():
            if w in list_words:
                words_frequency[w] += 1
        print('Line', count_line,':', words_frequency)


# In[26]:





# In[ ]:





# In[ ]:


Fix this


sns.set(style="white", context="talk")
rs = np.random.RandomState(8)

# Set up the matplotlib figure
f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7, 5), sharex=True)

# Generate some sequential data
x = np.array(list("ABCDEFGHIJ"))
y1 = np.arange(1, 11)
sns.barplot(x=x, y=y1, palette="rocket", ax=ax1)
ax1.axhline(0, color="k", clip_on=False)
ax1.set_ylabel("Sequential")

# Center the data to make it diverging
y2 = y1 - 5.5
sns.barplot(x=x, y=y2, palette="vlag", ax=ax2)
ax2.axhline(0, color="k", clip_on=False)
ax2.set_ylabel("Diverging")

# Randomly reorder the data to make it qualitative
y3 = rs.choice(y1, len(y1), replace=False)
sns.barplot(x=x, y=y3, palette="deep", ax=ax3)
ax3.axhline(0, color="k", clip_on=False)
ax3.set_ylabel("Qualitative")

# Finalize the plot
sns.despine(bottom=True)
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)

