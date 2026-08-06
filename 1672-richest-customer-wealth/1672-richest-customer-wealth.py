class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        a = []
        for i in range(len(accounts)):
            a.append(sum(accounts[i]))
        return max(a)    
                