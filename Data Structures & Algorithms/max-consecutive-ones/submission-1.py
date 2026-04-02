class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max = 0
        for i in nums:
            if i == 1:
                counter += 1
                if max < counter:
                    max = counter
            else:
                counter = 0
        
        return max