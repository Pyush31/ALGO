from helpers import *
 
# Helper Functions for Q (a simple Priority Queue)
# To Extract the Minimum from the Queue
def extractMin(Q):
    if Q == []:
        return None
    minimum = Vertex(0)
    for V in Q:
        if V.key < minimum.key:
            minimum = V
    return minimum
 
# To Check whether a vertex 'v' has a Vertex-Object in Q
def belongs(Q,v):
    for vertex in Q:
        if vertex.vertex == v:
            return True
    return False
 
# To Get the Vertex Object associated with vertex 'v'
def getVertex(Q,v): 
    for vertex in Q:
        if vertex.vertex == v:
            return vertex
    return None
 
 
# Prim's Algortihm that returns the Edges of the Minimum Spanning Tree
def prim(G):
    MST = []
    
    # Creating a Priority Queue
    Q = []
    for V in G.V:
        Q.append(Vertex(V))
 
    # Setting the First Vertex to Source
    Q[0].key = 0
    while Q != [] :
        # Gettng the Vertex in Q with the Minimum Key Value 
        u = extractMin(Q) 
        
        # Finding all the adjacent vertices of the vertex 'u'
        neighbours = G.adjacentVertices(u.vertex)
        
        # Findig the vertex with the least weight local to 'u' using Greedy Strategy
        for v in neighbours:
            _v = getVertex(Q,v)
            if _v is not None:
                if belongs(Q,v) and (_v.key > G.weight(u.vertex,v)):
                    _v.parent = u.vertex
                    _v.key = G.weight(u.vertex,v)
        Q.remove(u)
        # Getting the edge with the least weight that is not yet been selected
        selectedEdge = extractMin(Q)
        if selectedEdge is not None:
            MST.append((selectedEdge.parent,selectedEdge.vertex,selectedEdge.key))
    
    S = "\n" + "EDGES IN THE MST - (u, v, weight)" + "\n" + "-"*75 + "\n"
    for edge in MST:
        S += str(edge) + "\t"
        if (MST.index(edge)+1) % 5 == 0:
            S += "\n\n"
    S += "\n" + "-"*75
    return S
 
         
                
def main():
    # creating the graph Object 
    graph = Graph(7)
 
    # adding edges in the Graph using addEdge() method
    graph.addEdge(1,2,28)
    graph.addEdge(2,3,16)
    graph.addEdge(3,4,12)
    graph.addEdge(4,5,22)
    graph.addEdge(5,6,25)
    graph.addEdge(5,7,24)
    graph.addEdge(6,1,10)
    graph.addEdge(7,2,10)
    graph.addEdge(7,4,18)
    
    # displaying the Adjacency Matrix
    print(graph)   
 
    # get the MST
    print(prim(graph))
 
main()