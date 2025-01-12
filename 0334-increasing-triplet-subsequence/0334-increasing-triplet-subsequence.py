class Solution(object):
    def increasingTriplet(self, nums):
        first = float('inf')  # Initialize the smallest and 2nd smallest no
        second = float('inf')  

        for num in nums:
            if num <= first:  # Update 1st if current number is smaller
                first = num
            elif num <= second:  # Update 2nd if current number is larger than first but smaller than 2nd
                second = num
            else:  # If we find a number larger than second, we found the triplet
                return True

        return False
