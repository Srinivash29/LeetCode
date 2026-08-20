class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        a = []
        b = [''] * len(s)
        for i in s:
            a.append(i)
        for i in range(len(indices)):
            b[indices[i]] = a[i]
        c = ''.join(b)    
        return c    

        
            
        