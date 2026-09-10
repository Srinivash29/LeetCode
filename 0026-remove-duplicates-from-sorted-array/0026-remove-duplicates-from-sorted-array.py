class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        for i in range(len(nums)):
            if nums[i] not in a:
                a.append(nums[i])
            for i in range(len(a)):
                nums[i] = a[i]    
        return len(a)  
