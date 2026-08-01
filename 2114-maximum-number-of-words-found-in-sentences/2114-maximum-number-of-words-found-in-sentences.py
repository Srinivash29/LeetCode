class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        l = 0
        for i in sentences:
            r = i.split()
            if(len(r)>l):
                l = len(r)
        return l

        