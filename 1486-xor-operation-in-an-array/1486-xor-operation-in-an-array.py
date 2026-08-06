class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        i = 0
        a = 0
        b = 0
        nums = []
        while(i < n):
            a = start + 2 * i
            nums.append(a)
            i += 1
        for i in range(len(nums)):
            b ^= nums[i]
        return b       



        