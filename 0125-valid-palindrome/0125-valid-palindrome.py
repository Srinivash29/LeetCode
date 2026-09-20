class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        a = []
        b = ",.;:'/\"[]{}<>?-_=+!@#$%^&*\()`~ "
        for i in s:
            if i in b:
                continue
            else:
                a.append(i)
        a = "".join(a)
        return a == a[::-1]
                
               





        