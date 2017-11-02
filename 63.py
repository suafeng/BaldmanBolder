# Unique Paths II

# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.

# still simple, using negative number to count. First initilization, if in first
# row or column there is obstacle, just end at obstacle.
# Then update dp table as normal, if upper or left of a cell is obstacle, then
# only add from the side which is not obstacle. If both are obstacles, then do
# not update.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            obstacleGrid[0][i] = -1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            obstacleGrid[i][0] = -1
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if (obstacleGrid[i-1][j] != 1 or obstacleGrid[i][j-1] != 1) and obstacleGrid[i][j] != 1:
                    obstacleGrid[i][j] = min(obstacleGrid[i-1][j], obstacleGrid[i][j-1], obstacleGrid[i-1][j] + obstacleGrid[i][j-1])
        if obstacleGrid[-1][-1] == 1:
            return 0
        else:
            return -obstacleGrid[-1][-1]
