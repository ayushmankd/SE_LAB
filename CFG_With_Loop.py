# Generation Of CFG with Loop
from dfs import dfsPathGeneration
from CyclomaticComplexity import CC
from NumBoundedRegions import NBR
from listToMat_Graph import LtM
cfg = {}
curr = 1
nodes = {}
whileNode = None
ifNode = None                                                      
ifBlock = None                                                     
elseBlock = None 
considerWhile = False  
f = open("if_else_with_loop.txt", "r") 
if f.mode == 'r':
    contents = f.readlines()
    i = 0
    while i < len(contents):
        line = contents[i].strip('\n')
        # If "If" Statment is present
        if line.find("if") != -1:                                  
            curr += 1                                              
            nodes[curr] = [line]                                   
            ifNode = curr                                            
            ifBlock = curr + 1                                      
            elseBlock = ifNode                                     
            cfg[curr-1] = [curr]                                   
            cfg[curr] = [curr+1]                                   
            curr += 1  
        # If "Else" Statment is present
        elif line.find("else") != -1:                              
            curr += 1                                              
            elseBlock = curr                                       
            cfg[ifNode].append(curr)    
        # If Current Statement belongs to a If/Else Block
        elif line.startswith("  "):
            # If While Block is Present   
            if line.find("while") != -1:
                curr += 1
                nodes[curr] = [line]
                whileNode = curr
                cfg[curr-1] = [curr]
                curr += 1
                considerWhile = True
            # If Curr Statement belongs to the While Block
            elif line.startswith("      "):
                if curr in nodes:
                    nodes[curr].append(line)
                else:
                    nodes[curr] = [line]
                cfg[curr-1] = [curr]
            # If Statment belongs to If/Else Block Before While Block
            elif (not line.startswith("     ") and whileNode == None):
                if curr in nodes:
                    nodes[curr].append(line)
                else:
                    nodes[curr] = [line]
            # If Statement Belongs to If Block but after while Node
            # To check whether ifblock == elseblock approach works
            elif (not line.startswith("     ") and (whileNode != None) and (considerWhile)):
                cfg[curr] = [whileNode]
                curr += 1
                if curr in nodes:
                    nodes[curr].append(line)
                else:
                    nodes[curr] = [line]
                cfg[whileNode].append(curr)
                ifBlock = curr
                considerWhile = False
            # If Statement Belongs to Else Block but after while Node
            elif (not line.startswith("     ") and (whileNode != None) and (not considerWhile)):
                if curr in nodes:                                      
                    nodes[curr].append(line)
                else:
                    nodes[curr] = [line]
                pass
        # For Statements Upto the First "If" Statment
        elif (
            not line.startswith(" ") and 
            (ifNode == None) and 
            (elseBlock == None)):                                  
            if curr in nodes:                                      
                nodes[curr].append(line)
            else:
                nodes[curr] = [line]
            pass
        # For Statements after finishing if/else blocks
        elif (not line.startswith(" ") and (ifNode != None)):       
            curr += 1                                              
            if curr in nodes:                                      
                nodes[curr].append(line)
            else:
                nodes[curr] = [line]
            pass                                            
            if (ifNode != elseBlock):                               
                cfg[ifBlock] = [curr]                              
                cfg[elseBlock] = [curr]                            
            else:
                cfg[ifBlock] = [curr]                              
                cfg[ifNode].append(curr)
        i += 1
print ("Nodes: ", nodes)
print ("Adjacency Repn of CFG: ", cfg)
print ("Matrix Repn: ", LtM(cfg, nodes))
print ("Number of Bounded Regions are: ", NBR(cfg))
print ("Cyclomatic Complexity: ", CC(cfg, nodes))
# print (dfsPathGeneration(1, cfg))
path1 = [1, 2, 3, 4, 6, 8]
path2 = [1, 2, 3, 4, 5, 4, 6, 8]
path3 = [1, 2, 7, 8]
print ("Path: ", path1)
print ("Path: ", path2)
print ("Path: ", path3)