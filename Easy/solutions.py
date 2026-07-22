#problem no: 1

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]
                    break
#Problem no: 2
class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        for i in range(1,n+1):
            if(i%3 == 0 or i%5 == 0 or i%7 == 0):
                a+=i
        return a  