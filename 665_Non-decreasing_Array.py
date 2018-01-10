# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first
# 4
#  to
# 1
#  to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].

# try hard to think!

# there are only two situations.
# nums[i-2] <= nums[i] and nums[i-2] > nums[i]

# for first situation, let nums[i-1] = nums[i]
# for the second, let nums[i] = nums[i-1]

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True
        once = False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if once:
                    return False
                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                once = True
        return True
