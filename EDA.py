# coding: utf-8


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os #as os
import data_object

from os import path, getcwd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
from packages.graphical.generate_wordcloud import get_long_tweet_string

### Basic usage section

#print(op2)
#print(op2.shape)
#op2.head()
#print(op2.head())

                  
#op2['Text'].value_counts()
#op1[op2['Text'] == 'shit']

# Can be used to print all instead. Example parameters included
#with pd.option_context('display.max_rows', None):
#    print(op2)



### Assign variables with examples
op1 = pd.read_csv('test.csv') 
op2 = pd.read_csv('trump.csv', usecols=['Name', 'Text'])
op3 = pd.read_csv('Ntrump.csv', usecols=['Name', 'Text', 'Place']




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



# Generate WordCloud
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



sns.lmplot(x='Name', y='Text', data=op3)
 
# Alternative way
# sns.lmplot(x=df.Attack, y=df.Defense)

'
list_words = ['Trump'.casefold(), 'anal','house']
filename = op3

# Tokenizer. Comment or uncommment as necessary
rm = ",:;?/-!."

# with open(filename,'r') as fin:
#    for count_line, line in enumerate(fin,1):
#        clean_line = filter(lambda x: not (x in rm), line)
#        # To hold the counts of each word
#        words_frequency = {key: 0 for key in list_words}
#        for w in clean_line.split():
#            if w in list_words:
#                words_frequency[w] += 1
#        print('Line', count_line,':', words_frequency)


