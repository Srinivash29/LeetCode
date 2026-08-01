class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s = "abcdefghijklmnopqrstuvwxyz"
        count = 0
        for i in s:
            if i in sentence:
                count += 1
        return(count == 26)
                
        