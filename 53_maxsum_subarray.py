# Simple DP. The max sum ending at ith position is
# max(nums[i], maxsub(i-1)+nums[i])

def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = nums[0]
        rt_sum = curr
        for i in nums[1:]:
            curr = max(i, curr + i)
            rt_sum = max(rt_sum, curr)
        return rt_sum
