class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr1 = []
        arr2 = []
        arr3 = []
        for n1 in range(len(nums)-n):
            arr1.append(nums[n1])
        for n2 in range(n,n+n):
            arr2.append(nums[n2])    
        for n3 in range(n):
            arr3.append(arr1[n3])
            arr3.append(arr2[n3])

        return arr3          
            
        