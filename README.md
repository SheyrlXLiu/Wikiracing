# Wikiracing

Wikiracing is a Python command line tool to traverse a way from one Wikipedia page to another, using only links. This tool will return a list of titles that form a path between the source and destination through snetwork requests made to the WikiMedia API.

## Getting Started

The project utilized two methods to conduct the searching process: DFS and BFS. 

1. DFS (Depth-first search)

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

2. BFS (Breadth-first search)

Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

It uses the opposite strategy as depth-first search, which instead explores the node branch as far as possible before being forced to backtrack and expand other nodes.

### Prerequisites

Python 3.7.6

### Installing

1. In the terminal, copy and paste the command below:

```
git clone https://github.com/SheyrlXLiu/Wikiracing.git
```

2. Change the directory to Wikiracing by:

```
cd Wikiracing/
```

3. Install required modules by :

```
pip install -r requirements.txt
```

4. To start a search using DFS, type:

```
python DFS_crawler.py 
```
Then follow the instructions in the termial to input the start point and destination. 

5. To start a search using BFS, type:

```
python BFS_crawler.py 
```
Then follow the instructions in the termial to input the start point and destination. 


## References:

1. https://en.wikipedia.org/wiki/Depth-first_search

2. https://en.wikipedia.org/wiki/Breadth-first_search
