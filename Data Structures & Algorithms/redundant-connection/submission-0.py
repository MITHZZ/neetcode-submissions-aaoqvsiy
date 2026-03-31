class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        # edgesconn = {i:[] for i in range(1,len(edges)+1)}
        # for s, d in edges:
        #     edgesconn[s].append(d)
        # for s, d in edges:
        #     edgesconn[d].append(s)
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par):
            if visit[node]:
                return True

            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (n + 1)

            if dfs(u, -1):
                return [u, v]
        return []
        


            
        
        