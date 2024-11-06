class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()  # Sort the array for two-pointer approach
        left, right = 0, len(nums) - 1
        op = 0
        
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1  # Decrease right pointer
            elif nums[left] + nums[right] < k:
                left += 1   # Increase left pointer
            else:
                op += 1     # A valid pair is found
                left += 1
                right -= 1  # Move both pointers inward
        
        return op
