class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
  
            width = right - left
            h = min(height[left], height[right])
            current_area = width * h

            
            max_area = max(max_area, current_area)

            # Move the pointer with the smaller height to try and find a larger area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
