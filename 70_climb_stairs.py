# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you
# climb to the top?
#
# Note: Given n will be a positive integer.

# Dynamic programming

# we can go from prev stair, or prev prev stair.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev_p = 1
        prev = 2
        curr = None
        for i in range(3, n+1):
            curr = prev_p + prev
            prev_p = prev
            prev = curr
        return curr
