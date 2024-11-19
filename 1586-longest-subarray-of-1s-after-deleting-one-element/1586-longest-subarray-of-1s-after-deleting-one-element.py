class Solution(object):
    def longestSubarray(self, nums):
            # Left pointer of the sliding window
        l = 0  
        # Variable to store the maximum length of subarray found
        max_length = 0  
        # Counter to track the number of zeros in the current window
        zero_count = 0  
        
        # Loop through each element in the array with the right pointer `r`
        for r in range(len(nums)):
            # If the current element is 0, increment the zero counter
            if nums[r] == 0:
                zero_count += 1
            
            # If the number of zeros in the current window exceeds 1, we need to shrink the window
            while zero_count > 1:
                # Check the element at the left pointer
                if nums[l] == 0:
                    # If it's a zero, decrement the zero counter
                    zero_count -= 1
                # Move the left pointer to the right to shrink the window
                l += 1
            
            # Calculate the length of the current valid window
            # Subtract 1 because one element must be deleted
            max_length = max(max_length, r - l)
        
        # Return the longest subarray length found
        return max_length