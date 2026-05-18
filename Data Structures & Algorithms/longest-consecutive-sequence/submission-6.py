class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxLen = 0
        currLen = 1
        sorted_num = sorted(list(set((nums))))
        for n in range(len(sorted_num)):
            if sorted_num[n] != sorted_num[-1]:
                if sorted_num[n + 1] == sorted_num[n] +1:
                    currLen += 1
                else:
                    if currLen > maxLen:
                        maxLen = currLen
                    currLen = 1
        if currLen > maxLen:
            maxLen = currLen    
        print(sorted_num)
        return maxLen