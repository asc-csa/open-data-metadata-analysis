import json
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def generateWordcloud(files, output): 
    
    file_jsonl = [name for name in files if name.endswith('.jsonl')]
    file_jsonl = file_jsonl[0]
    infile = file_jsonl
    
    stopwords = ("the", "of", "for", "on" , "and", "at", "a", "up", "in", "as", "s", "to", "are", "by", "This", "i", "is", "it", "from", "or", "be", "an", "was", "these", "which", "with", "that", "also", "its", "were", "has", "they", "who", "have", "until", "during", "based", "Canadian", "Space", "Agency", "use", "reports", "data", "CSA", "plan", "program", "year", "act", "report", "plans", "over", "Canada", "provide", "project", "department", "each")
    
    data = []
    descriptions = []
    dataset_name_en = []
        
    with open(infile, encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line)) #load per line, needed for the jsonl format
    
    for d in data:
        dataset_name_en.append(d['title_translated']['en'])
        descriptions.append(d['notes'])
    
    datasetName_words = " ".join(dataset_name_en) + " "
    description_words = " ".join(descriptions) + " "
    
    datasetNameWordcloud = WordCloud(width=1000, height=600,
                          background_color='white',
                          stopwords=stopwords,
                          max_words = 1000,
                          collocations = False,
                          min_font_size=10).generate(datasetName_words)
    
    descriptionWordcloud = WordCloud(width=1000, height=600,
                          background_color='white',
                          stopwords=stopwords,
                          max_words = 1000,
                          collocations = False,
                          min_font_size=10).generate(description_words)
    
    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(datasetNameWordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    
    plt.gcf()
    dataset_name = output + '\datasetName_wordCloud.png'
    plt.savefig(dataset_name)
    plt.show()
    
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(descriptionWordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    
    plt.gcf()
    description_name = output + '\descriptions_wordCloud.png'
    plt.savefig(description_name)
    plt.show()




