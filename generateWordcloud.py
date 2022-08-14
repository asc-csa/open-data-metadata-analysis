import numpy as np
import json

import pandas as pd
from os import path
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


infile = 'C:/Users/harain/Desktop/PythonFiles/Metadata/ckan_metadata_dump_20220526.jsonl'
outfile = 'df1.csv'

stopwords = ("the", "of", "for", "on" , "and", "at", "a", "up", "in", "as", "s", "to", "are", "by", "This", "i", "is", "it", "from", "or", "be", "an", "was", "these", "which", "with", "that", "also", "its", "were", "has", "they", "who", "have", "until", "during", "based", "Canadian", "Space", "Agency", "use", "reports", "data", "CSA", "plan", "program", "year", "act", "report", "plans", "over", "Canada", "provide", "project", "department", "each")
# canadian space agency

data = []
descriptions = []
dataset_name_en = []
    
with open(infile, encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line)) #load per line, needed for the jsonl format

print(descriptions)

for d in data:
    dataset_name_en.append(d['title_translated']['fr'])
    descriptions.append(d['notes'])

print(descriptions)
comment_words = " ".join(descriptions) + " "

wordcloud = WordCloud(width=1000, height=600,
                      background_color='white',
                      stopwords=stopwords,
                      max_words = 1000,
                      collocations = False,
                      min_font_size=10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.gcf()
plt.savefig('descriptions_wordCloud.png')
plt.show()


