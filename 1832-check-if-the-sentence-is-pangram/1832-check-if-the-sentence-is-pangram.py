class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        a = set(sentence)
        return (len(a) == 26)
                
        