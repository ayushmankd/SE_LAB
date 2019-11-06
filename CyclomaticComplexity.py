# The Cyclomatic Complexity Algo

# Finding the Cyclomatic Complexity using the Formala
# CC = NumEdges - NumNodes + 2 * Connected Components 
def CC(cfg, nodes):
    numEdges = 0 
    for i in cfg:
        numEdges += len(cfg[i])
    return (numEdges - len(nodes) + 2) #Since there is only 1 Connected Component