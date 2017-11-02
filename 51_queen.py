# n queen
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.

# for a queen placed at (x, y), for position (p, q), if p+q=x+y or p-q=x-y, this
# position can be attacked by the queen. Based on this, we place the queen line
# by line. we have array queens, queens[i], i is the ith line, queens[i] is the
# queen's postion in this line. Do backtracing using recursive function. Add
# queens to the result if we have a qualified queen array. xy_sum and xy_dif
# store each queen's p+q and p-q data.

class Solution(object):
    # result, queens, xy_sum, xy_dif are arrays
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
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        self.getQueen(result, [], [], [], n)
        ret = []
        for so in result:
            tmp = []
            for q in so:
                line = ['.' for i in range(n)]
                line[q] = 'Q'
                tmp.append(''.join(line))
            ret.append(tmp)
        return ret
        # return result
