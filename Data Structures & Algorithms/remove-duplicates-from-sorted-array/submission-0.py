class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize left pointer 'l'
        l = 1

        # Traverse the array nums with right pointer 'r'
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1

        return l