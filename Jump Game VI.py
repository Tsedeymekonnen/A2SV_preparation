class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        d = deque([n-1])
        for i in range(n-2, -1, -1):
            if d[0] - i > k: d.popleft()
            nums[i] += nums[d[0]]
            while len(d) and nums[d[-1]] <= nums[i]: d.pop()
            d.append(i)
        return nums[0]
