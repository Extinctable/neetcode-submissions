# Brute Force Solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Inialize an empty array to temporarily store valid elements 
        tmp = []
        for i in range(len(nums)):
            if nums[i] != val:
                tmp.append(nums[i])
            else:
                continue
        for j in range(len(tmp)):
            nums[j] = tmp[j]

        return len(tmp)
