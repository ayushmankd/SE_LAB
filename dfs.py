# The Path Generation Algo using DFS
def dfsPathGeneration(start, graph):
    explored = [start]
    paths = []
    currPath = []
    while (len(explored) > 0):
        currPath.append(explored[-1])
        if explored[-1] in graph:
            curr = explored[-1]
            for i in graph[explored[-1]]:
                explored.append(i)
            explored.remove(curr)
        else:
            newPath = currPath[:]
            paths.append(newPath)
            last = currPath.pop()
            explored.remove(last)
            for i in reversed(currPath):
                if len(graph[i]) != 2:
                    currPath.remove(i)
                else:
                    break
    return paths