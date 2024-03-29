# c5 
import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2]=wt
        self.adjMatrix[v2][v1]=wt
    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2):
            return 
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=1
    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False
    def printGraph(self):
        print(self.adjMatrix)
    #c7(dfs) c13
    def dfs(self):
        # visited=[False for i in range(self.nVertices)]
        visited={}
        for i in range(self.nVertices):
            visited[i]=False
        # print(type`(visited))
        # self.dfsHelper(0,visited)
        for i in range(self.nVertices):
            if(not visited[i]):
                self.dfsHelper(i,visited)
    def dfsHelper(self,startingVertice,visited):
        print(startingVertice)
        visited[startingVertice]=True
        for i in range(self.nVertices):
            if(self.adjMatrix[startingVertice][i] and  not visited[i]):
                self.dfsHelper(i,visited)  
    # c8 c13
    def bfsHelper(self,sv,visited):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while q.empty() is False:
            ele=q.get()
            print(ele)
            for i in range(self.nVertices):
                if(self.adjMatrix[ele][i]>0 and visited[i] is False):
                    q.put(i)
                    visited[i]=True
    def bfs(self):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if(not visited[i]):
                self.bfsHelper(i,visited)

    # c11
    def hasPath(self,v1,v2):
        if(self.adjMatrix[v1][v2] >0):
            print(True)
            return True
        else:
            visited=[False for i in range(self.nVertices)]
            q=queue.Queue()
            q.put(0)
            visited[0]=True
            while q.empty()== False:
                ele=q.get()                
                for i in range(self.nVertices):
                    if(self.adjMatrix[ele][i]>0 and visited[i]==False):
                        q.put(i)
                        visited[i]=True
            if(visited[v2]==True):
                print(True)
                return True
            else:
                print(False)
                return False

g=Graph(9)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(3,2)
g.addEdge(2,4)
g.addEdge(2,0)
g.addEdge(6,0)
# g.addEdge(7,0)
# g.addEdge(8,0)
# g.dfs()
# g.bfs()
# g.hasPath(1,7)