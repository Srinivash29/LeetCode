class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        s = s.split()
        for i in s:
            a.append("".join(reversed(i)))
        return " ".join(a)
            
        
        