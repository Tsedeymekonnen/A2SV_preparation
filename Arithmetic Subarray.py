class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = []
        for i in range(len(l)):
            arr = sorted(nums[l[i]:r[i]+1])
            diff = [arr[j+1] - arr[j] for j in range(len(arr) - 1)]
            if len(set(diff)) == 1:
                 result.append(True)
            else:
                result.append(False)
        return result  
