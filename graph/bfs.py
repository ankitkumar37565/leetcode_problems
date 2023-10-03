from queue import Queue
from typing import List
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        ans = []
        
        #boolean list to mark all the vertices as not visited.
        vis = [False for i in range(V)]
        
        #creating a queue for BFS and pushing first vertex in queue.
        q = Queue(maxsize = 0)
        q.put(0)
        
        #initially we mark first vertex as visited(true).
        vis[0] = True
        
        while(q.empty() == False):
            
            #adding front element in output list and popping it from queue.
            v = q.get()
            ans.append(v)
            
            #traversing over all the connected components of front element.
            for i in adj[v]:
                
                #if they aren't visited, we mark them visited and add to queue.
                if(vis[i] == False):
                    vis[i] = True
                    q.put(i)
                    
        #returning the output list.
        return ans
        
        