from bs4 import BeautifulSoup
import requests
import json
from collections import deque

def get_title(wikipedia_url):
    html_file = requests.get(wikipedia_url).content.decode()
    soup = BeautifulSoup(html_file, 'html.parser')
    wikipeida_title = soup.find('title')
    print(wikipeida_title.string.replace(' - Wikipedia', ''))

def get_all_titles(wikipeida_title):
    if ' ' in wikipeida_title:
        parse_title = wikipeida_title.replace(' ', '_')
    else:
    	parse_title = wikipeida_title
    URL = 'http://en.wikipedia.org/w/api.php'
    params = {
    'action':'query',
    'prop':'links',
    'titles': wikipeida_title,
    'pllimit':'max',
    'format':'json',
    }
    request = requests.get(URL, params)
    json_file = json.loads(request.content)
    
    try:
        pageid = list(json_file['query']['pages'])[0]
        links = json_file['query']['pages'][pageid]['links']
        titles = set(title['title'] for title in links)
        return titles
    except KeyError as e:
        titles = set()
        return titles
    while 'continue' in json_file:
        params['plcontinue'] = json_file['continue']['plcontinue']
        request = requests.get(URL, params)
        json_file = json.loads(r.content)
        links = json_file['query']['pages'][pageid]['links']
        titles = titles.union(set(title['title'] for title in links))
        return titles

def BFS(title1, title2, depth):
    if title1 == title2:
        return title1
    queue = deque([(title1, [title1])])
    while queue:
        vertex, path = queue.popleft()
        sub_titles = get_all_titles(vertex)
        
        for next in sub_titles - set(path):
            if next == title2:
                return path + [next]
            elif len(path) < depth:
                queue.append((next, path + [next]))
    return

def visited_path():
    path = [title2]
    if title1 == title2:
        return title1
    while title2 != title1:
        title2 = parent[title2]
        path.insert(0, title2)


'''
The crawl funciton of the project. 
The function will transfer any urls to titles then revoke the DFS function to start the searching process. 
'''
def crawl(title1, title2):
    if "http" in title1:
        title1 = str(get_title(title1))
    else: 
        title1 = str(title1)
    if "http" in title2:
        title2 = str(get_title(title2))
    else: 
        title2 = str(title2)
    for depth in range(10):
        route = BFS(title1, title2, depth)
        if route:
            print(*route, sep='\n')
            return route
    return 'Unable to find route up to depth=10'


'''
Main execution of the project. The command will ask users to type the start point and the destination. 
Then the program will start crawling. 
'''
if __name__ == '__main__':
    title1 = str(input("Please type in your start point: "))
    title2 = str(input("Please type in your start point: "))
    print('***Working***')
    crawl(title1, title2)
    print('***Finished***')
    