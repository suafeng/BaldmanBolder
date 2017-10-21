# Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating
# characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.

# The first thing in my mind is something like DP. After I write it out I
# realize it is just look like DP.

# Maintain a list to record what characters we currently have, if current
# character is not in the list, append it to the list and see whether we should
# update the max count. If it is already in the list, then only pick the part
# of the list that does not have this character and append this character to it.
# Since in the second case the length of sub will not increase, no need to
# try to update count.

def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        sub = [s[0]]
        count = 1
        for c in s[1:]:
            if c not in sub:
                sub.append(c)
                count = max(len(sub), count)
            else:
                for i in range(len(sub)):
                    if sub[i] == c:
                        break
                sub = sub[i+1:]
                sub.append(c)
        return count

# The second method is to use a hashtable, character for key and position for
# value!

def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        max_count = 1
        ht = dict()
        ht[s[0]] = 0
        low = 0
        for i in range(1, len(s)):
            if s[i] in ht and low <= ht[s[i]]:
                low = ht[s[i]] + 1
            ht[s[i]] = i
            max_count = max(max_count, i - low + 1)
        return max_count

def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        max_count = 1
        ht = dict()
        ht[s[0]] = 0
        low = 0
        for i in range(1, len(s)):
            if s[i] in ht:
                low = max(low, ht[s[i]] + 1)
            ht[s[i]] = i
            max_count = max(max_count, i - low + 1)
        return max_count
