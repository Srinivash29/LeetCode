class Solution(object):
    def canAliceWin(self, nums):
        a = 0
        b = 0
        for i in nums:
            if(i < 10):
                a += i
            else:
                b += i
        if(a > b):
            return True
        elif(b > a):
            return True
        else:
            return False                       
           


        