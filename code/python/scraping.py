# this file scrape top 5 sentences of a target vocabulary from Google search
# method source: https://www.pingshiuanchua.com/blog/post/scraping-search-results-from-google-search

# setting up the scope of search

# constraints:
    # source website: yourdictionary.com [ONLY]
    # the UnicodeError() issue unresolved! some words cannot get encoded properly

import urllib

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

### set up google query string ###
wordlist = [ "esoteric", "erudite","calumny", "fallacy"]  # must be a list of strings!
    #issue_1:  "loquacious" encounter a UnicodeErrort

#scrape all sentences of the target word from yourdictionary.com
def scrape(word,num):
    query = urllib.parse.quote_plus(word)  # format into URL encoding
    number_result = num  # number of sentences to scrape from
    ua = UserAgent()
    #google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
    google_url = "https://sentence.yourdictionary.com/" + query
    response = requests.get(google_url, headers={"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")
    result_div = soup.find_all('div', attrs={'class': 'li_content'})
    # return a SET of tags, each containing one sentence of the target word
    result_div = list(result_div)  #convert the set into a list
    n = max(len(result_div), number_result)
    sentences = []
    for i in range(n):
        sentences.append(result_div[i])
    return sentences


word = wordlist[3].encode('utf-8')
scrapped = scrape(word, 4)
print(scrapped)








#
#
# ### structure scrapped results ###
# links = []
# titles = []
# descriptions = []
#
# for r in result_div:
#     # check if each element is present, else raise exception
#     try:
#         link = r.find('a', href=True)
#         title = r.find('div', attrs={'class': 'vvjwJb'}).get_text()
#         description = r.find()('div', attrs={'class': 'co8aDb gsrt'}).get_text()
#
#         # Check to make sure everything is present before appending
#         if link != '' and title != '' and description != '':
#             links.append(link['href'])
#             titles.append(title)
#             descriptions.append(description)
#     # Next loop if one element is not present
#     except:
#         continue
