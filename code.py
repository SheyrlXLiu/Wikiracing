from bs4 import BeautifulSoup
import requests
import json




'''
link_list = []
for item in all_links:
	link = item.get('href')
	link_list.append(link)

link_list = list(filter(lambda link_str: 'http' in str(link_str), link_list))
link_list = list(filter(lambda link_str: 'en.wikipedia' in str(link_str), link_list))
'''

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
	    print("Didn't find the wikipedia page of " + wikipeida_title + "!")
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

    stack = [(title1, [title1])]
    while stack:
        (vertex, path) = stack.pop()
        sub_titles = get_all_titles(vertex)
        print(sub_titles)
        if title2 in sub_titles:
            return title2

        for next in sub_titles - set(path):
            if next == title2:
                return path + [next]
            elif len(path) < depth:
                stack.append((next, path + [next]))
    return

def crawl(title1, title2):
    for depth in range(10):
        route = BFS(title1, title2, depth)
        if route:
            print(title1)
            print(route)
            return route
    return 'Unable to find route up to depth=9'
'''
def main():
    title1 = str(input("Please enter the start point: "))
    title2 = str(input("Please enter the end point: "))
    crawl(title1, title2)



if __name__ == '__main__':
    main()
    # test_cases()
'''
crawl('Seattle', 'Thayers')