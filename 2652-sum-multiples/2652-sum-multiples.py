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
        