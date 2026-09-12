class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=set(nums)
        for i in a:
            if(nums.count(i) == 1):
                return i
                
                                 