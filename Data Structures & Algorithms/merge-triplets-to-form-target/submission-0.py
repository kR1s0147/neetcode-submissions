class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if not triplets or not target:
            return False
        res = [-1 ] * 3
        for t in range(len(triplets)):
            if triplets[t][0] > target[0] or triplets[t][1] > target[1] or triplets[t][2] > target[2]:
                continue
            if triplets[t][0] == target[0]:
                res[0]=1
            if triplets[t][1] == target[1]:
                res[1] = 1
            if triplets[t][2] == target[2]:
                res[2] = 1

        for i in res:
            if i == -1:
                return False
        return True