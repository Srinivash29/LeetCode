class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a = {'L': 0,'U': 0,'R': 0,'D': 0}
        for i in moves:
            a[i] += 1
        return (a['L'] == a['R'] and a['U'] == a['D'])    

        
        
