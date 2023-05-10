import nltk
from wordcloud import WordCloud
from matplotlib import pyplot as plt

def gen_wordcloud(text_string):
    cloud = WordCloud(width=1600, height=800, max_font_size=200).generate(text_string)
    plt.figure(figsize=(12,10))
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
               
