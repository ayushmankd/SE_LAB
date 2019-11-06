# To Calculate Number of Bounded Regions in the Graphs
def NBR(cfg):
    numBoundedRegions = 0
    # for i in cfg:
    #     if len(cfg[i]) < 2: #If there are no two edges originating the skip
    #         continue
    #     else:
    #         # If there are 2 edges from this node and both this edges end at the same node
    #         # then its a Bounded Region
    #         if cfg[cfg[i][0]] == cfg[cfg[i][1]]: 
    #             numBoundedRegions += 1
    count = {}
    for i in cfg:
        if len(cfg[i]) == 1:
            if cfg[i][0] in count:
                count[cfg[i][0]] += 1
            else:
                count[cfg[i][0]] = 1
    for i in count:
        if count[i] == 2:
            numBoundedRegions += 1
    return numBoundedRegions