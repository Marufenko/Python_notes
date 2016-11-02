class Node(object):
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self,src,dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + ' -> ' + self.dest.getName()

class Diagraph(object):
    '''one direction'''
    def __init__(self):
        self.edges={}
    def addNode(self,node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node]=[]
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self,node):
        return self.edges[node]
    def hasNode(self,node):
        return node in self.edges
    def getNode(self,name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + ' -> ' + dest.getName() + '\n'
        return result[:-1] #omit final newline
        
class Graph(Diagraph): #Graph is subclass of Diagraph
    '''two direction'''
    def addEdge(self,edge):
        Diagraph.addEdge(self,edge)
        rev = Edge(edge.getDestination(),edge.getSource())
        Diagraph.addEdge(self,rev)
        
#for popualtion
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston','Providence','New York','Chicago','Denver','Phoenix','Los Angeles'):
        g.addNode(Node(name)) #create 7 nodes
    g.addEdge(Edge(g.getNode('Boston'),g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'),g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'),g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'),g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'),g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'),g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'),g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'),g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'),g.getNode('Boston')))
    return g
    
#to build in one direction
#print(buildCityGraph(Diagraph))
    
#to build in two direction
print(buildCityGraph(Graph))
