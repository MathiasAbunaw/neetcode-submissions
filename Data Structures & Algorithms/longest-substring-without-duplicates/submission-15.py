class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        value = []
        maxi = 0
        for let in s:
            if let not in value:
                value.append(let)
            else:
                maxi = max(maxi, len(value))
                while let in value:
                    value.pop(0)
                value.append(let)
        return max(maxi, len(value))