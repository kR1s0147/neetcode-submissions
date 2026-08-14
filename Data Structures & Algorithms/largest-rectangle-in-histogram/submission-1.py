class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
            n = len(heights)
            maxArea =0 

            for i in range(n):

                rightmost =i+1
                while rightmost < n and heights[rightmost] >= heights[i]:
                    rightmost +=1

                leftmost = i
                while leftmost >=0  and heights[leftmost] >= heights[i]:
                    leftmost-=1

                rightmost -=1
                leftmost +=1
                maxArea  =max(maxArea , heights[i] * (rightmost - leftmost +1))
            return maxArea

