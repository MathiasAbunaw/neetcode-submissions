class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        curr = 0
        for i in range(len(heights)):
            for j in range(len(heights)-1,i,-1):
                curr = min(heights[i], heights[j]) * (j -i)
                if (curr > res):
                    res = curr
        return res