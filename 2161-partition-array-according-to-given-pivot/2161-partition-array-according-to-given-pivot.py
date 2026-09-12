class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        a = []
        b = []
        c = []
        for i in nums:
            if i<pivot:
                a.append(i)
            elif i == pivot:
                c.append(i)    
            else:
                b.append(i)
        return a+c+b        

        