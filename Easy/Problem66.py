class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=""
        for i  in digits:
            a += str(i)
        b = str(int(a) + 1)
        c = []

        for i in b:
            c.append(int(i))

        return c