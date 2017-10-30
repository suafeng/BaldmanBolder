# find a unit to partition the whole staff

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        holder = ["" for i in range(numRows)]
        for i in range(len(s)):
            tmp = i % (2*numRows - 2)
            if tmp < numRows:
                holder[tmp]+=s[i]
            else:
                tmp = tmp - (numRows-1)
                holder[numRows - 1 - tmp]+=s[i]
        result = ""
        for i in range(len(holder)):
            result += holder[i]
        return result
