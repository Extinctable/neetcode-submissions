class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 # Initialize a counter variable
        max = 0 # Initialize a var to hold the max number of consecutive 1's
        # Iterate through the array 'nums'
        for i in range(len(nums)):
            # For each step, if the value of the index is equal to 1, we increment the counter
            if nums[i] == 1:
                counter += 1
                # If the counter is greater than the max, assign the value to max
                if counter > max:
                    max = counter
            # Reset the counter if a value in the index is 0
            else:
                counter = 0
        return max
        