'''
Question: Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Thoughts: We could do a bidirectional search - but I guess thats for the shortest path, but we are fine with any route.. 
So probably if we have an adjacency matrix, we can scan all the nodes in one row. 
So its O(k) for each node... where k is the node. 

Or we could basically scan the adjacency list..  

So basically it comes down to the DFS and BFS methods.. Could discuss pros and cons of it. 

'''