from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt 
import pandas as pd 
from tweet_feed import Feed
from basic_cleaner import BasicCleaner
import data_object
import csv
from PIL import Image  
from os import path, getcwd 
import numpy as np




# // Use either
#file_path = "../pickle_saved_data"

# /// Or: V
# // VVV Change file name locally VVV
FilePath = "../DataCollection/DCMERGE/191114-14_53_41--191211-21_37_33"
sentiment_range = [float(-1), float(1)]

def get_long_tweet_objects():
    feed = Feed()
    queue_stream = feed.disk_get_tweet_queue(FilePath)
    data_objects = [data_object.get_dataobj_converted(tweet) for tweet in queue_stream]
    for obj in data_objects: BasicCleaner.autocleaner(obj,sentiment_range, True)
    return data_objects

def get_long_tweet_string():
    long_string = [obj.text*(obj.valid_sentiment_range) for obj in get_long_tweet_objects()]
    return " ".join(long_string)

# # def generate_wordcloud():
# #     WC = WordCloud(width = 800, height = 800, 
# #                     background_color ='white',  
# #                     min_font_size = 10).generate(get_long_tweet_string()) 
    
# #     # plot WC                       
# #     plt.figure(figsize = (8, 8), facecolor = None) 
# #     plt.imshow(WC) 
# #     plt.axis("off") 
# #     plt.tight_layout(pad = 0) 
# #     plt.show() 

def write_csv(_filename):
    with open(_filename, 'w', newline='') as csvfile:
        obj_writer = csv.writer(csvfile, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)

        obj_list = get_long_tweet_objects()
        obj_writer.writerow(["name"] + ["txt"] + ["coord"] + ["places"] + ["hashtags"] + ["alphatags"] + ["sentiment"])
        for obj in obj_list:
            obj_writer.writerow([obj.name] + 
                                [obj.text] + 
                                [obj.coordinates] +
                                [obj.place] + 
                                [obj.hashtags] +
                                [obj.alphatags] + 
                                [obj.valid_sentiment_range])

#/ Under construct
#write_csv(FilePath)

# /under construct
def WC():

  #/ Test path
  file_path = open('dank.csv').read()
  sentiment_range = [float(-1), float(1)]
  d = getcwd()
  mask = np.array(Image.open(path.join(d, "mask.jpg")))

  WC = WordCloud(background_color="black", max_words=40000, mask=mask, max_font_size=80, random_state=42)
  WC.generate(file_path)
        
  image_colors = ImageColorGenerator(mask)  
  plt.figure(figsize = (15, 10)) 
  plt.imshow(WC.recolor(color_func=image_colors), interpolation="bilinear") 
  plt.axis("off")
  plt.tight_layout(pad = 0) 
  WC.to_file("../wordcloud.png") 

  plt.show() 

WC()



 #/ ACTUAL PATH INSIDE WC:
  #file_path = open(FilePath).read()
  #sentiment_range = [float(-1), float(1)]

# Create stopword list inside WC:
  #topwords = set(STOPWORDS)
  ###stopwords.update(["A", "B", "C", "D", "E"])
  ###stopwords.add(custom_stopwords_list.txt)