# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

# The thing is to restrict the list of the for sides: up bound, right bound,
# down bound, left bound. Each time finish one strip, update the corresponding
# bound. if the bound goes to the strip that has been scanned, means job done,
# return the result

def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rt = []
        m = len(matrix)
        if m == 0:
            return rt
        n = len(matrix[0])

        u, r, d, l = 0, n - 1, m - 1, 0
        while True:
            for col in range(l, r + 1, 1):
                rt.append(matrix[u][col])
            u += 1
            if u > d:
                break
            for row in range(u, d + 1, 1):
                rt.append(matrix[row][r])
            r -= 1
            if r < l:
                break
            for col in range(r, l - 1, -1):
                rt.append(matrix[d][col])
            d -= 1
            if d < u:
                break
            for row in range(d, u - 1, -1):
                rt.append(matrix[row][l])
            l += 1
            if l > r:
                break
        return rt
