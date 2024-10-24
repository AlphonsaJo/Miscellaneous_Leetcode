class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0  # Pointer for the current position to check

        # Process the array
        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1  # Move the pointer for non-zero elements

        return nums


