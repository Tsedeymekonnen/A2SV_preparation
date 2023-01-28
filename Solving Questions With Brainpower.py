class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        dp = [0]*(len(questions)+1)
        for i in range(len(questions) - 1, -1, -1):
             points = questions[i][0]
             jump = questions[i][1]
             dp[i] = max(points + dp[min(jump + i + 1, len(questions))], dp[i + 1])
        return dp[0];  
