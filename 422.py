# description is too long, so I will not put it here

# Search line by line. This problem is to get you think about the corner cases.

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if len(words) != len(words[0]):
            return False
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True
