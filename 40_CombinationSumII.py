# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# Now we can have duplicate candidates. To prevent duplicate result, when a
# number goes into the recursive, do not let other same candicate to enter
# recursive in this level.

class Solution(object):
    def helper(self, result, curr, candidates, target):
        if target == 0:
            result.append(curr)
            return
        if target < 0:
            return
        if len(candidates) == 0:
            return
        self.helper(result, curr + [candidates[-1]], candidates[:-1], target - candidates[-1])
        first_in = len(candidates) - 1
        cursor = first_in - 1
        while cursor >= 0 and candidates[cursor] == candidates[cursor+1]:
            cursor -= 1
        self.helper(result, curr[:], candidates[:cursor+1], target)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.helper(result, [], candidates, target)
        return result
