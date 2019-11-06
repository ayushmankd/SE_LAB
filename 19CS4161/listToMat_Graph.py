# Program to Make a List Repn of Graph to its Matrix Repn
def LtM(graph, nodes):
    mat = [[0 for i in range(len(nodes))] for j in range(len(nodes))]
    for i in graph:
        for j in graph[i]:
            mat[i-1][j-1] = 1
    return mat