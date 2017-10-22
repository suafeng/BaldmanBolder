# find whether a array contains duplicated element.

# method: use a hash table, then done

def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ht = dict()
        for n in nums:
            if n not in ht:
                ht[n] = True
            else:
                return True
        return False
