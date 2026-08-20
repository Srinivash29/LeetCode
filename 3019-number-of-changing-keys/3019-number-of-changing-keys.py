class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lower()
        a = 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                a += 1
        return a    
        

