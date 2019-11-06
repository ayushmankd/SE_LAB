# Generation Of CFG of a Program with Conditional 
# Statements without Loop Statements
from dfs import dfsPathGeneration
from CyclomaticComplexity import CC
from NumBoundedRegions import NBR
from listToMat_Graph import LtM
# from PIL import Image
cfg = {}                                                           #The Resultant Graph will be Stored Here
curr = 1                                                           #The Current node index being checked
nodes = {}                                                         #The Nodes of the Resultant Graph
ifNode = None                                                      #Node Num of the if Node
ifBlock = None                                                     #Node Num of the if Block (Nodes inside if Block)
elseBlock = None                                                   #Node Num of the else Block (Nodes inside else Block)
f = open("prgm_without_loop.txt", "r") 
if f.mode == 'r':
    contents = f.readlines()
    i = 0
    while i < len(contents):                                       #Iterating over each line of the Given Program
        line = contents[i].strip('\n')
        if line.find("if") != -1:                                  #If Current Line contains "if"
            curr += 1                                              #Increment Curr Node index
            nodes[curr] = [line]                                   #Store this "Condtion" in the Nodes DS
            ifNode = curr                                          #ifNode variable is updated  
            ifBlock = curr + 1                                     #ifBlock variable is updated 
            elseBlock = ifNode                                     #Currently else block isn't present
            cfg[curr-1] = [curr]                                   #New Edge from Previous Node to this if Node
            cfg[curr] = [curr+1]                                   #New Edge from this Node to if block
            curr += 1                                              #Current Node is Updated
        elif line.find("else") != -1:                              #If Current Line contains "else"
            curr += 1                                              #Increment Curr Node index
            elseBlock = curr                                       #elseBlock is updated to store this
            cfg[ifNode].append(curr)                               #adding of edge from ifnode to this edge block
        elif line.startswith(" "):                                 #If the curr line is of if/else block
            if curr in nodes:                                      #Just append it to current Node
                nodes[curr].append(line)
            else:
                nodes[curr] = [line]
            pass
        elif (
            not line.startswith(" ") and 
            (ifNode == None) and 
            (elseBlock == None)):                                  #Statements before if/else statements
            if curr in nodes:                                      #Just append it to current Node
                nodes[curr].append(line)
            else:
                nodes[curr] = [line]
            pass
        elif (not line.startswith(" ") and (ifNode != None)):      #Statements after if/else 
            curr += 1                                              #Increment current node
            if curr in nodes:                                      #Store Current Node
                nodes[curr].append(line)
            else:
                nodes[curr] = [line]
            pass                                            
            if (ifNode != elseBlock):                              #If "If" and "Else" statements both are present 
                cfg[ifBlock] = [curr]                              #Add Edge to this Node from if block
                cfg[elseBlock] = [curr]                            #Add Edge to this Node from else Block
            else:
                cfg[ifBlock] = [curr]                              #Else just add Edge to this Node from if Block
                cfg[ifNode].append(curr)
        i += 1
print ("Nodes: ", nodes)
print ("Adjacency Repn of CFG: ", cfg)
print ("Matrix Repn: ", LtM(cfg, nodes))
print ("Number of Bounded Regions are: ", NBR(cfg))
print ("Cyclomatic Complexity: ", CC(cfg, nodes)) 
paths = dfsPathGeneration(1, cfg)
for path in paths:
    print ("Path: ", path)
