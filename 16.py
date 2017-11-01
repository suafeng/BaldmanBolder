# 3Sum Closest

# the idea is similar to 3SUM. Fix the first number, and use two pointer to
# scan. Jump through the duplicate ones.

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = sum(nums[0:3])
        for i in range(len(nums)-2):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                curr_sum = (nums[i] + nums[lo] + nums[hi])
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1

                if curr_sum > target:
                    hi -= 1
                elif curr_sum < target:
                    lo += 1
                else:
                    return target
        return closest
