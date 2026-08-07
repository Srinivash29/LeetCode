import math
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod = 1
        for i in nums:
            prod *= i

        return 1 if prod > 0 else -1 if prod < 0 else 0 
        