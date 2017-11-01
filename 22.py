# Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# Backtrace. Use recursive function to build all combination. In the recursive
# function, set the constrains.

class Solution(object):
    def backtrace(self, result, curr, ln, rn, n):
        if ln + rn == 2*n and ln == rn:
            result.append(curr)
        if ln < n:
            self.backtrace(result, curr+'(', ln+1, rn, n)
        if rn < ln:
            self.backtrace(result, curr+')', ln, rn+1,n)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.backtrace(result, '', 0, 0, n)
        return result
