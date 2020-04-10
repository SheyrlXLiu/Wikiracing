from bs4 import BeautifulSoup
import requests

url1 = 'Segment'

html_file = requests.get("https://en.wikipedia.org/wiki/" + url1).content.decode()
soup = BeautifulSoup(html_file, 'html.parser')
all_links = soup.find_all('a')
link_list = []
for item in all_links:
	link = item.get('href')
	link_list.append(link)

link_list = list(filter(lambda link_str: 'http' in str(link_str), link_list))
link_list = list(filter(lambda link_str: 'en.wikipedia' in str(link_str), link_list))
print(link_list)
