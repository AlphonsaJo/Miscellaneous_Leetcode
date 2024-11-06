class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()  
        left, right = 0, len(nums) - 1
        op = 0
        
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1  
            elif nums[left] + nums[right] < k:
                left += 1   
            else:
                op += 1     
                left += 1
                right -= 1  
        
        return op
