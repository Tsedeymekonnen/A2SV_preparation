class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 == 0 or len(nums) == 1:
            return True

        res = [0] * len(nums);
        for i in reversed(xrange(len(nums))):
            res[i] = nums[i]
            for j in xrange(i+1, len(nums)):
                res[j] = max(nums[i] - res[j], nums[j] - res[j - 1])

        return res[-1] >= 0      
