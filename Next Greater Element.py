class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nextGreat = {}
        stack = []

        for num in nums2:
          while stack and stack[-1] < num:
            nextGreat[stack.pop()] = num
          stack.append(num)

        return [nextGreat.get(num, -1) for num in nums1]
