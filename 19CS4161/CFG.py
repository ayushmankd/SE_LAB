import re
import listToMat_Graph
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
breakStatements = re.compile('if|while|for|else|elif')
f = open('MinMaxMatrix.py', mode='r')
contents = f.readlines()
nodes = {}
graph = {}
i = 0
currNode = 1
while i < len(contents):
    line = contents[i]
    # Check whether the line contains any break statment like if, else, while, for etc.
    # If not then add the line to current node
    if not breakStatements.search(line):
        if currNode in nodes:
            nodes[currNode].append(line)
        else:
            nodes[currNode] = [line]
        i += 1
    # Do this if we encounter any break statements
    # Add a edge from the current node to the next node
    else:
        if currNode in graph:
            graph[currNode].append(currNode+1)
        else: 
            graph[currNode] = [currNode+1]
        currNode += 1
if len(graph) == 0:
    graph[1] = []
print (nodes)
for i in nodes:
    G.add_node(i)
for i in graph:
    G.add_edges_from(graph[i])
nx.draw(G)
plt.show()
print (graph)
print (listToMat_Graph.LtM(graph, nodes))
if len(graph) == 1:
    nbr = 0
    print ("Number Of Bounded Regions: ", nbr)
    print ("List of Independent Paths: ", 0)