class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        prereq = {}
        self.cycle = True
        for i,j in prerequisites:
            if i not in prereq.keys():
                prereq[i] = []
            prereq[i].append(j)

        def dfs(num,visited):

            if num in visited:
                self.cycle = False
                return

            if num not in prereq.keys():
                return 

            visited.append(num)

            for i in prereq[num]:
                if i in visited:
                    self.cycle = False
                    return
                dfs(i,visited)

            visited.pop()
            
        for i in prereq.keys():
            dfs(i,[])
                
        return self.cycle
            