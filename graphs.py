"""Notes from Interactive Python

edges - lines
vertices - nodes or points 
sparse graph - not much information stored in graphs

Graph() creates a new, empty graph.
addVertex(vert) adds an instance of Vertex to the graph. 
addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
getVertex(vertKey) finds the vertex in the graph named vertKey.
getVertices() returns the list of all vertices in the graph.
in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.
"""


"""Implementing graphs with adjacency list(Uses dictionary class to implement- each vertices keeps list of other 
vertice connections)."""

from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

class Vertex:
    def __init__(self,key):
        #creates key and empty dictionary 
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        #adds connecting verticies with value that is the weight of the edge or connection between thte two
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        #returns list of vertices connected to this vertex
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        #get value/weight of edge from this vertex to a connecting vertex 
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        #creates a graph with empty dictionary and sets number of vertices to zero
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        #increments the vertices counter, instaniates a new vertex object, adds that new vertex object to graph dictionary. 
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        #gets vertex list and searches to see if vertex is in list(and therefore in the graph)
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        #returns True if vertex is in vertList(therefore in graph) 
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        #after checkig if vertices exsist/adding vertices if they don't, creates edge/connection by adding to vertex dictionary 
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        #returns list of vertices
        return self.vertList.keys()

    def __iter__(self):
        #allows list of vert values to be interable 
        return iter(self.vertList.values())

"""Breadth First Search
-Easiest for searchign a graph.
-Finds all vertices that are k distance from s before finding vertices that are k + 1 distance from s(buidls a tree one layer at a time)
-for this example, the vertices are color coded: 
    White = undiscovered
    Gray = discovered(but not all related vertices have been discovered)
    Black = explored(all related vertices have been discovered)
-Uses Queue to explore because last in first out is import to maintain order of vertices to be explored
-added to Vertex class: distance, predecessor, and color (part of the pythonds library)
Big O notation: O(n) with n being the number of vertices to transverse 
"""
# from pythonds.graphs import Graph, Vertex
# from pythonds.basic import Queue

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)#set predecessor to none in order to make this the root of the tree
  vertQueue = Queue() #instantiates a queque 
  vertQueue.enqueue(start) #adds to queque 
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue() #removes first vertex added to the queque
    for nbr in currentVert.getConnections(): #gets the vertex's list of connections and loops through the list
      if (nbr.getColor() == 'white'):#if unexplored 
        nbr.setColor('gray')#set to explored 
        nbr.setDistance(currentVert.getDistance() + 1) #Gives weight/distance of vertex to root. Can be considered layers of tree 
        nbr.setPred(currentVert)#set predecessor/parent vertex
        vertQueue.enqueue(nbr) #places back in queue to explore if vertex has other connections/children 
    currentVert.setColor('black') #explored 

"""Knight Tour 
This looks for a tour to visit every square on the board exactly once. 
"""
from pythonds.graphs import Graph, Vertex
def knightTour(n,path,u,limit): # n = depth in search tree; path = list of vertices visted; u = vertex to explore; limit= number of nodes on path
        u.setColor('gray')#color set to indicate exploration 
        path.append(u)#add vertex/node to path
        if n < limit:
            nbrList = orderByAvail(n)#gets list of connected nodes of current vertex/node with shortest route 
            i = 0 #counter 
            done = False #when recursition hits the bottom of the stack and returns 
            while i < len(nbrList) and not done:#loops through all children of a vertex/list
                if nbrList[i].getColor() == 'white':#if unexplored
                    done = knightTour(n+1, path, nbrList[i], limit)#recurse with current node/vertx
                i = i + 1#increment count
            if not done:  # prepare to backtrack
                path.pop() #pop this path if it is a dead end
                u.setColor('white') #return to unexplored/unvisited vertex/square. 
        else:
            done = True #stops loop when returned to indicate a deadend
        return done

    
def orderByAvail(n):
    resList = []
    for v in n.getConnections():# gets all connected nodes for current node
        if v.getColor() == 'white': # if unexplored
            c = 0 # counter
            for w in v.getConnections(): #get child node connections 
                if w.getColor() == 'white': #if unexplored
                    c = c + 1 #number of connections
            resList.append((c,v)) #puts a tuple in the list with the child nodes and number of child node's connections
    resList.sort(key=lambda x: x[0])#sorts tuples for node with least connections 
    return [y[1] for y in resList]#returns n's child node with least children/connections 

"""Depth First Search 

""" 
from pythonds.graphs import Graph
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

from pythonds.graphs import PriorityQueue, Graph, Vertex
def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)

def prim(G,start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
          newCost = currentVert.getWeight(nextVert) \
                  + currentVert.getDistance()
          if nextVert in pq and newCost<nextVert.getDistance():
              nextVert.setPred(currentVert)
              nextVert.setDistance(newCost)
              pq.decreaseKey(nextVert,newCost)


"""Color Graph
Notes from: https://www.cs.princeton.edu/courses/archive/fall06/cos341/handouts/graph1.pdf

A graph is colorable if each vertex can be assigned one color so that adjacent vertices get different colors. 
A color graph is k(the maximum degree of any vertex in the graph) the number of colors will be k + 1 
Induction Hypothesis:
    Let P(n) b the proposition that an n-vertext graph with maximum degree at most k is (k + 1)-colorable
    A 1-vertex graph has maximum degree 0 and is 1-colorable, so P(1) is true 
Complete graph or clique: graph with all possible edges 
Aconnected component of a graph is a maximal connected subgraph of the graph.Maximal means you can't add any
    nodes or edges to the subgrpah without making it be disconnected. 
"""

"""Matchings 
Notes from: https://www.cs.princeton.edu/courses/archive/fall06/cos341/handouts/graph2.pdf

Matching Problems: Given a graph where the edges represent compatibility, the goal is to create the maximum number
    of compatible pairs
    -a matching is a subgraph of a Graph where every node has degree 1. The matching consists of edges that do not share nodes
    -A matching f a graph G = (V, E) is perfect if it has |V|/2 edges 
    -Arise in context of a bipartie graph(a graph whose vertices can be divided into two disjoint sets. 
    -The goal is to find the perfect matching wiht the minimum weight 
The weight of matching M is the sum of the wieghts on the edges in M. The min-weight matching for a graph G is the perfect
    matching for G with minimum weight (if it exists)
    -If there is a better match than ones created, causes instablity 
"""

"""file:///Users/hollymalm/Desktop/C2U4GT.pdf """
"""file:///Users/hollymalm/Desktop/graphtheory.pdf """
"""file:///Users/hollymalm/Desktop/graphs_1_print.pdf """