class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seem = []
        for i in nums:
            if i in seem:
                return True
            else:
                seem.append(i)
        return False


        