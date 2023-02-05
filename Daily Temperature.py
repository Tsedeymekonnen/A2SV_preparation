class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result =[0 for _ in range(n)]
        s = []
        for i in range(0,n):
            while (len(s)>0) and temperatures[i]> temperatures[s[len(s)-1]]:
              index = s[len(s)-1]
              s.pop()
              result[index] = i-index
            s.append(i)
        return list(result)      
