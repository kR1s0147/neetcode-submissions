class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , u = 1 , max(piles)
        res= 0

        while l<=u:
            k = (l+u)//2
            time = 0 
            for pile in piles:
                time+= math.ceil(float(pile) / k)
            if time > h:
                l = k+1
            elif time <= h:
                res = k
                u = k-1
        return res