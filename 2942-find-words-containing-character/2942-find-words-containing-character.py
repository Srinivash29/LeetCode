class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        a = []
        for index,value in enumerate(words):
            if x in value:
                a.append(index)
        return a    


