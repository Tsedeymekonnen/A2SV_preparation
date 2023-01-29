class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(arr) ,0,-1) :
            res = arr.index(i)
            arr[:res + 1] = arr[:res + 1][::-1]
            arr[:i] = arr[:i][::-1]  
            result.append(res + 1)
            result.append(i) 
        return result 
