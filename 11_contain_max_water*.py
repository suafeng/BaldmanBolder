# two pointer.
# from the widest bucket, if the inner bucket can contain more water only if
# their effective height (min(left_h, righth)) is larger than previous one.
# check all these bucket.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo, hi = 0, len(height) - 1
        water = 0
        while lo < hi:
            effective_h = min(height[lo], height[hi])
            water = max((hi - lo) * effective_h, water)
            while lo < hi and height[lo] <= effective_h:
                lo += 1
            while lo < hi and height[hi] <= effective_h:
                hi -= 1
        return water
