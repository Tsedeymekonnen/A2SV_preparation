class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        result = []
        for i in num:
          while k and result and result[-1] > i: 
         
            result.pop() 
            k = k -1 
      
          result.append(i) 
         
        return ''.join(result).lstrip('0') [:-k or None]  or '0'
