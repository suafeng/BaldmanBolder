# remove duplicate from sorted array
# the idea is to use two pointers. One points to the place the number shoule be
# written on, the other points to the current number we are examing.

def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        prev = None
        for c in nums:
            if prev == c:
                prev = c
                continue
            nums[length] = c
            length += 1
            prev = c
        return length
