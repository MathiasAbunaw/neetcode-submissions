class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value = []
        for i in range(len(nums)):

            for j in range(i +1, len(nums)):
                if (j not in value) and (i not in value):
                    if (nums[j] + nums[i]) == target:
                        value.append(i)
                        value.append(j)
        return value