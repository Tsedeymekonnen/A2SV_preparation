class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        stor = [0] * n
        for i in bookings:
          stor[i[0] - 1] += i[2]
          if i[1] < n:
            stor[i[1]] -= i[2]
        for j in range(1, n):
          stor[j] += stor[j - 1]

        return stor
