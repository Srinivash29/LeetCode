class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        nums3 = []
        for i in range(len(nums1)):
            nums3.append(nums2[i] - nums1[i])
        return nums3[0]