class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        s = str(num)
        for i in s:
            if(int(s)%int(i) == 0):
                count += 1
        return count        
