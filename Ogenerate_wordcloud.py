from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt 
import pandas as pd 
from tweet_feed import Feed
from basic_cleaner import BasicCleaner
import glob
import os #as os
import csv
import twitterset_scaling_helper
import data_object




### // init twitterset_scaling_helper

#q = twitterset_scaling_helper
#q

#### // GET FILES 2

# path = r"..\\DataCollection\\TestFolder_mergedFromDataColl\\"
# all_files = glob.glob(os.path.join(path))

# df2 = (pd.read_csv(f) for f in all_files)
# cdf = pd.concat(df2, ignore_index=True, sort=False)



# print(cdf)

# write_csv



#all_files = glob.glob(os.path.join(path, "*.csv"))

#df2 = (pd.read_csv(f) for f in all_files)
#cdf = pd.concat(df2, ignore_index=True, sort=False)


### // GET FILES




input("Data Collection created, press enter to clean and CSV")
### // Write CSV

dir_name = 'C:/Users/Joakim/Desktop/SkoleTing/Studio/Datacollection/DCMERGE'
extension = ".zip"


os.chdir(dir_name)                              # // change directory from working dir to dir with files

for item in os.listdir(dir_name):               # // loop through items in dir
    if item.endswith(extension):                # // check for ".zip" extension
        file_name = os.path.abspath(item)  

file_path = '../DataCollection/DCMERGE/191114-14_53_41--191211-21_37_33'
sentiment_range = [float(-1), float(1)]

def get_long_tweet_objects():
    feed = Feed()
    queue_stream = feed.disk_get_tweet_queue(file_path)
    data_objects = [data_object.get_dataobj_converted(tweet) for tweet in queue_stream]
    for obj in data_objects: BasicCleaner.autocleaner(obj,sentiment_range, True)
    return data_objects



def get_long_tweet_string():
    long_string = [obj.text*(obj.valid_sentiment_range) for obj in get_long_tweet_objects()]
    return " ".join(long_string)


def write_csv(_filename):
    with open(_filename, 'w', newline='') as csvfile:
        obj_writer = csv.writer(csvfile, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)

        obj_list = get_long_tweet_objects()
        obj_writer.writerow(["name"] + ["txt"] + ["coord"] + ["places"] + ["hashtags"] + ["alphatags"] + ["sentiment"])
        for obj in obj_list:
            try:
                obj_writer.writerow([obj.name] + 
                                    [obj.text] + 
                                    [obj.coordinates] +
                                    [obj.place] + 
                                    [obj.hashtags] +
                                    [obj.alphatags] + 
                                    [obj.valid_sentiment_range])
            except:
                pass


write_csv('dank.csv')

input("press enter to continue..")


with open("dank.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(" ".join(row))



## // GET FILES

# file_path = r"../DataCollection/TestFolder_mergedFromDataColl/" 
# sentiment_range = [float(-1), float(-0.5)]

#print(file_path)

### // UNHASH

file_path = 'dank.csv'
sentiment_range = [float(-1), float(1)]


# Create stopword list:
### stopwords = set(STOPWORDS)
### stopwords.update(["drink", "now", "wine", "flavor", "flavors"])

# Generate WordCloud

# WC = WordCloud(width = 800, height = 800, 
#                background_color ='white',  
#                min_font_size = 10).generate(file_path)
  
# plot WC                       
# plt.figure(figsize = (8, 8), facecolor = None) 
# plt.imshow(WC) 
# plt.axis("off") 
# plt.tight_layout(pad = 0) 
# WC.to_file("../wordcloud.png")

# plt.show() 

input("press enter to create wordcloud...")

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
from os import path, getcwd
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

wcdir = 'C:\\Users\\Joakim\\Desktop\\SkoleTing\\Studio\\Twitter_Master\\'
os.chdir(wcdir)

# True file path
file_path = open('dank.csv').read()
sentiment_range = [float(-1), float(1)]

# Test File
# file_path = open('../DataCollection/Wine/winemag-data_first150k.csv')

# Create stopword list:
#topwords = set(STOPWORDS)
###stopwords.update(["A", "B", "C", "D", "E"])
###stopwords.add(custom_stopwords_list.txt)

# img
d = getcwd()
mask = np.array(Image.open(path.join(d, "mask.jpg")))

# Generate WordCloud

WC = WordCloud(background_color="black", max_words=40000, mask=mask, max_font_size=80, random_state=42)

#WC = WordCloud(width = 800, height = 800, 
 #               background_color ='blue',  
  #              min_font_size = 1)
WC.generate(file_path)

# plot WC                     
image_colors = ImageColorGenerator(mask)  
plt.figure(figsize = (15, 10)) 
plt.imshow(WC.recolor(color_func=image_colors), interpolation="bilinear") 
plt.axis("off")
plt.tight_layout(pad = 0) 
#WC.to_file("../wordcloud.png") 

plt.show() 

