class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            guessNum = target-numbers[i]
            if guessNum in numbers:
                if(numbers.index(guessNum) != i):
                    if (numbers.index(guessNum)+1) not in res:
                        res.append(i+1)
                        res.append(numbers.index(guessNum)+1)
        return res