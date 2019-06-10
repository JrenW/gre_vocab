import urllib

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
query = "market"
google_url = "https://sentence.yourdictionary.com/" + query
response = requests.get(google_url, headers={"User-Agent": ua.random})
soup = BeautifulSoup(response.text, "html.parser")
result_div = soup.find_all('div', attrs={'class': 'li_content'})
# return a SET of tags, each containing one sentence of the target word
result_div = result_div
print(result_div)
