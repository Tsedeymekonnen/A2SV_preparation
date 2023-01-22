class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        count = 0 
        stack = []
        for i in pushed:
          stack.append(i)
          while stack and count < len(popped) and stack[-1] == popped[count]:
              stack.pop()
              count += 1
        return count == len(popped)
