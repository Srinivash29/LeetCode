class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        pod = 1
        sod = 0
        for i in str(n):
            pod *= int(i)
            sod += int(i)
        return pod - sod    


        