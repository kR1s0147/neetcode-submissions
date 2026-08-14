from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, curr: int) -> int:
            if curr == amount:
                return 1
            if curr > amount or i == len(coins):
                return 0

            # Option 1: take coin[i] again (stay at i)
            # Option 2: skip coin[i] (move to i+1)
            return dfs(i, curr + coins[i]) + dfs(i + 1, curr)

        return dfs(0, 0)