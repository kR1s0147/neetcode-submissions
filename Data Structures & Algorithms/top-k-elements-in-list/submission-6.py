class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
    
    # Create a bucket where index represents frequency
        d2 = [[] for _ in range(len(nums) + 1)]
        for num, freq in d.items():
            d2[freq].append(num)
        
        r = []
        # Iterate through the bucket in reverse order
        for i in range(len(d2) - 1, 0, -1):
            for num in d2[i]:
                r.append(num)
                if len(r) == k:
                    return r