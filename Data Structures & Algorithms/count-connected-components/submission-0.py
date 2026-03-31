class unionfind:

    def __init__(self,n):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x1,x2):
        p1,p2 = self.find(x1),self.find(x2)

        if p1 == p2 :
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else : 
            self.parent[p1] = p2
            self.rank[p2] += 1

        return True




class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = unionfind(n)

        for u,v in edges:
            uf.union(u, v)

        res = []

        for i in range(n):
            res.append(uf.find(i))
        
        return len(set(res))


        