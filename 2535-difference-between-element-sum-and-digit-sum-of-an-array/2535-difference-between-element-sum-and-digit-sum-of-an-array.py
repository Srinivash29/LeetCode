class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        for i in nums:
            a += i
            while(i>9):
                b += i%10
                i //= 10
            b += i
        return abs(a-b)        


       
                
         
          

        

        