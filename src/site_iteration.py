from bs4 import BeautifulSoup
import urllib3
import re
from pprint import pprint

http = urllib3.PoolManager()

url_list = [
    "https://www.wsj.com/news/markets",
    "https://www.msn.com/en-us/money/markets",
    "https://www.zacks.com/stocks/",
    "https://seekingalpha.com/",
    "https://www.investopedia.com/markets/",
    "https://finance.yahoo.com/",
    "https://www.fool.com/investing-news/",
    "https://www.thestreet.com/",
    "https://finviz.com/news.ashx","https://webcache.googleusercontent.com/search?q=cache:cUa6ax_c7wMJ:https://seekingalpha.com/market-news/all+&cd=1&hl=en&ct=clnk&gl=us",
    "http://vestywaves.com/?category=markets",
    "http://streetsleuth.com/#tab1",

]

url = "http://streetsleuth.com/#tab1"

response = http.request('GET', url)
soup = BeautifulSoup(response.data, "lxml")

# Storing Titles
###############
title_list = []
for link in soup.findAll('a', attrs={'href': re.compile("^http(s*)://")}):
    try:
        print(link.get('href'))
        link_response = http.request('GET', link.attrs['href'])
        link_soup = BeautifulSoup(link_response.data, "lxml")
        link_title = link_soup.find('title').text
        title_list.append(link_title)
    except:
        continue

title_list = list(set(title_list))
pprint(title_list)


# # Storing Article Body
# #####################
# article_list = []
# for link in soup.findAll('a', attrs={'href': re.compile("^http(s*)://")}):
#     print(link.get('href'))
#     link_response = http.request('GET', link.attrs['href'])
#     link_soup = BeautifulSoup(link_response.data, "lxml")
#     try:
#         link_article = link_soup.find(
#             'div', attrs={'class': re.compile("article-content.*")}
#         ).findAll('p')
#     except AttributeError:
#         continue
#     article_str = ""
#     for sentence in link_article:
#         article_str += sentence.text
#     article_list.append(article_str)
#
# article_list = list(set(article_list))
