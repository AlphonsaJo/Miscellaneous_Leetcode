'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Explanation:

    Initially, low, mid, and high are set to 0, 0, and n-1, respectively.
    The algorithm iterates through the array, ensuring that:
        All elements before low are 0s.
        All elements between low and mid are 1s.
        All elements after high are 2s.
    By the end of the iteration, the array will be sorted in-place with all 0s first, followed by all 1s, and then all 2s.

This algorithm runs in O(n) time and uses O(1) extra space, making it optimal for this problem.

'''
