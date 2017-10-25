# Given m arrays, and each array is sorted in ascending order. Now you can pick
# up two integers from two different arrays (each array picks one) and calculate
# the distance. We define the distance between two integers a and b to be their
# absolute difference |a-b|. Your task is to find the maximum distance.
#
# Example 1:
# Input:
# [[1,2,3],
#  [4,5],
#  [1,2,3]]
# Output: 4
# Explanation:
# One way to reach the maximum distance 4 is to pick 1 in the first or third
# array and pick 5 in the second array.
# Note:
# Each given array will have at least 1 number. There will be at least two
# non-empty arrays.
# The total number of the integers in all the m arrays will be in the range
# of [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].

# the thought is, the result must be in 1) max and min, or 2) second max and
# min, or 3) max and second min. Therefore I need to these numbers.

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
#         be careful about initialization
        min_n = float('inf')
        min_n_index = -1
        max_n = -float('inf')
        max_n_index = -1
        for i in range(2):
            if arrays[i][0] < min_n:
                min_n = arrays[i][0]
                min_n_index = i
            if arrays[i][-1] > max_n:
                max_n = arrays[i][-1]
                max_n_index = i
        min_2_n_index = 1 - min_n_index
        min_2_n = arrays[min_2_n_index][0]
        max_2_n_index = 1 - max_n_index
        max_2_n = arrays[max_2_n_index][-1]


        for i in range(2, len(arrays)):
            if arrays[i][0] < min_n:
                min_2_n = min_n
                min_2_n_index = min_n_index
                min_n = arrays[i][0]
                min_n_index = i
            if arrays[i][-1] > max_n:
                max_2_n = max_n
                max_2_n_index = max_n_index
                max_n = arrays[i][-1]
                max_n_index = i
            if arrays[i][0] < min_2_n and i != min_n_index:
                min_2_n = arrays[i][0]
                min_2_n_index = i
            if arrays[i][-1] > max_2_n and i != max_n_index:
                max_2_n = arrays[i][-1]
                max_2_n_index = i

        if(max_n_index != min_n_index):
            return max_n - min_n

        return max(max_n - min_2_n, max_2_n - min_n)

# The problem is that, this is too fucking tedious to implement.
# In the solution, we can see a better way to do this.
# The idea is keep max and min, and most importantly, the result. Update result,
# when a[-1] - min or max - a[0] is larger than current result, then update
# min and max if necessary.

# God damn it, it is much easier and simpler than my implementation.

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_n = arrays[0][0]
        max_n = arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            res = max(res, arrays[i][-1] - min_n, max_n - arrays[i][0])
            min_n = min(min_n, arrays[i][0])
            max_n = max(max_n, arrays[i][-1])

        return res
