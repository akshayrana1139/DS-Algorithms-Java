'''
Question: List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
(e.g., if you have a tree with depth D, you'lf have D linked lists).

Thoughts: So basically we need to get away from the parents and children now, and we basically just store the nodes at each depth.
So its a BFS and keep adding everything to a new linked list as soon as the depth changes. 

Oh no wait.. BFS wont work for us in case the nodes are not connected.. We want to scan nodes of the entire tree for now. 
So we do need to maintain the level as a variable. 

We could do post-order traveral but it again needs to be modified. 



NEED TO GET BACK ON THIS





'''