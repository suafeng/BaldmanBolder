# n queen II

# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of
# distinct solutions.

# algorithm is the same with n queen I, but we only return the length of result
# now

class Solution(object):
    def getQueen(self, result, queens, xy_sum, xy_dif, n):
        if len(queens) == n:
            result.append(queens)
            return
        # search row by row
        i = len(queens)
        for j in range(n):
            if j not in queens and i+j not in xy_sum and i-j not in xy_dif:
                # the following is not correct, since each time we need to pass a new
                # instance of queens, xy_sum, xy_dif array. Otherwise we are always operating on
                # the same array, which is totally wrong
                # queens.append(j)
                # xy_sum.append(i+j)
                # xy_dif.append(i-j)
                self.getQueen(result, queens + [j], xy_sum + [i+j], xy_dif + [i-j], n)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = []
        self.getQueen(result, [], [], [], n)
        return len(result)
        
