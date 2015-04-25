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


# from pythonds.graphs import Graph, Vertex
# from pythonds.basic import Queue

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')

from pythonds.graphs import Graph, Vertex
def knightTour(n,path,u,limit):
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections())
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:  # prepare to backtrack
                path.pop()
                u.setColor('white')
        else:
            done = True
        return done

    
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]



    
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

