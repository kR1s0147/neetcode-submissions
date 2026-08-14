class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        def checkcycle(num,parent):
            if num in visited:
                return False
            visited.add(num)
            for i in graph[num]:
                if i == parent:
                    continue
                if not checkcycle(i,num):
                    return False
            return True
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            visited = set()
            if not checkcycle(list(graph.keys())[0],-1):
                return [u,v]

        return []