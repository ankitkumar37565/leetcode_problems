class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # initialize a visited list to keep track of visited nodes
        visited=[0]*V
        # initialize an empty list to store the DFS traversal
        values=[]
        # call the dfs function to perform DFS traversal
        self.dfs(0,adj,visited,values)
        # return the DFS traversal list
        return values
    
    # DFS function to perform depth-first search
    def dfs(self,node,adj,visited,values):
        # mark the current node as visited
        visited[node]=1
        # append the current node to the DFS traversal list
        values.append(node)
        
        # visit all the adjacent nodes of the current node
        for i in adj[node]:
            # if the adjacent node is not visited, recursively call the dfs function
            if visited[i]==0:
                self.dfs(i,adj,visited,values)
