class Solution(object):
    def findDifference(self, nums1, nums2):
        res = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        x = nums1.difference(nums2)
        y = nums2.difference(nums1)

        res.append(x)
        res.append(y)
        return res
        