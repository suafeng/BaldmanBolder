# combination sum

# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]

# backtracing
# the idea is you can use current candidate, or not. Set the stop condition.
# Then done.

class Solution(object):
    def helper(self, result, curr, candidates, target):
        if target == 0:
            result.append(curr)
            return
        if target < 0:
            return
        if len(candidates) == 0:
            return
        self.helper(result, curr + [candidates[-1]], candidates[:], target - candidates[-1])
        self.helper(result, curr[:], candidates[:-1], target)


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # top down
        result = []
        candidates.sort()
        self.helper(result, [], candidates, target)
        return result
