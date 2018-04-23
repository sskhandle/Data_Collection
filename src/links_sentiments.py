# Find links in a web page


# Get all links from webpage
############################
from bs4 import BeautifulSoup
import urllib3
import re
from pprint import pprint

http = urllib3.PoolManager()

url = "http://arstechnica.com"

response = http.request('GET', url)
soup = BeautifulSoup(response.data, "lxml")

# Storing Titles
################
# title_list = []
# for link in soup.findAll('a', attrs={'href': re.compile("^http(s*)://")}):
#     print(link.get('href'))
#     link_response = http.request('GET', link.attrs['href'])
#     link_soup = BeautifulSoup(link_response.data, "lxml")
#     link_title = link_soup.find('title').text
#     title_list.append(link_title)
#
# title_list = list(set(title_list))
# pprint(title_list)


# Storing Article Body
#####################
article_list = []
for link in soup.findAll('a', attrs={'href': re.compile("^http(s*)://")}):
    print(link.get('href'))
    link_response = http.request('GET', link.attrs['href'])
    link_soup = BeautifulSoup(link_response.data, "lxml")
    try:
        link_article = link_soup.find(
            'div', attrs={'class': re.compile("article-content.*")}
        ).findAll('p')
    except AttributeError:
        continue
    article_str = ""
    for sentence in link_article:
        article_str += sentence.text
    article_list.append(article_str)

article_list = list(set(article_list))
# pprint(article_list)




# link_list = soup.findAll('a', attrs={'href': re.compile("^http(s*)://")})
#
# sample_link = link_list[45]
#
# link_response = http.request('GET', sample_link.attrs['href'])
# link_soup = BeautifulSoup(link_response.data, "lxml")
# link_title = link_soup.find('title').text
#
# article_str = ""
# link_article = link_soup.find(
#     'div', attrs={'class': re.compile("article-content.*")}
# ).findAll('p')
#
# for sentence in link_article:
#     article_str += sentence.text
#
# print(article_str)


############################


# Using NLTK
###########################
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# sample_text = [
# "Great place to be when you are in Bangalore.",
# "The place was being renovated when I visited so the seating was limited.",
# "Loved the ambience, loved the food",
# "The food is delicious but not over the top.",
# "Service - Little slow, probably because too many people.",
# "The place is not easy to locate",
# "Mushroom fried rice was tasty"
# ]

si = SentimentIntensityAnalyzer()
score_list = []
for text in article_list: #title_list:
    print(text)
    score = si.polarity_scores(text)
    if score['compound'] == 0.0:
        continue
    # score_list.append(score['pos'])
    # score_list.append(score['neg']*-1)
    score_list.append(score['compound'])
    print('Sentiment Score: {}'.format(score))
    print ()

print (score_list)
print (sum(score_list))

#############################


