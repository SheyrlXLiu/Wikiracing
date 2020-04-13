from bs4 import BeautifulSoup
import requests
import json


start = 'Louisiana_State_University'
if " " in start:
	start.replace(" ", "_")
wikipedia_url = "https://en.wikipedia.org/wiki/" + start
html_file = requests.get(wikipedia_url).content.decode()
soup = BeautifulSoup(html_file, 'html.parser')
title = soup.title.string

all_links = soup.find_all('a')
link_list = []
for item in all_links:
	link = item.get('href')
	link_list.append(link)

link_list = list(filter(lambda link_str: 'http' in str(link_str), link_list))
link_list = list(filter(lambda link_str: 'en.wikipedia' in str(link_str), link_list))

def get_title(wikipedia_url):
	"""
    Return article's Wikipedia URL.
    INPUT:
        title -- string title of article.
    OUTPUT:
        fullurl -- string url of article.
    """
	html_file = requests.get(wikipedia_url).content.decode()
	soup = BeautifulSoup(html_file, 'html.parser')
	wikipeida_title = soup.title.string

def get_url(wikipeida_title):
    if ' ' in wikipeida_title:
        wikipeida_title = wikipeida_title.replace(' ', '_')
        API = 'http://en.wikipedia.org/w/api.php'
        params = {
        'action':'query',
        'prop':'info',
        'inprop':'url',
        'titles': wikipeida_title,
        'format':'json'
        }
        request = requests.get(API, params)
        json_file = json.loads(request.content)
        pageid = list(json_file['query']['pages'].values())[0]['pageid']
        fullurl = list(json_file['query']['pages'].values())[0]['fullurl']
        return fullurl

def DLS(start, end, depth):
    """
    Depth Limited Search is an implementation of Depth First Search with a
    limited depth. Continually search through child nodes in a last-in-first-out
    (LIFO) order until the desired end node is found.
    INPUT:
        start -- string title of starting article
        end -- string title of ending article
        depth -- integer depth to limit Search
    OUTPUT:
        path -- list of titles in sequence, when path is found
        OR
        None -- when path is not found
    Reference:
        https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search#Algorithm
    """
    if start == end:
        return [start]

    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()

        child_nodes = get_children(vertex)
        if end in child_nodes:
            return path + [end]

        for next in child_nodes - set(path):
            if next == end:
                return path + [next]
            elif len(path) < depth:
                stack.append((next, path + [next]))
    return

get_url('New Orleans')
