class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        num1 = len(security)
        num2 = [0] * num1 
        num3 = [0] * num1
        for i in range(1,num1 ):
            if security[i - 1] >= security[i]:
                 num2[i] = num2[i - 1] + 1 
        for i in range(num1 - 2, -1, -1):
            if security[i] <= security[i + 1]:
                num3[i] = num3[i + 1] + 1       
        return [i for i, (a, b) in enumerate(zip(num2, num3))
            if a >= time and b >= time]  
