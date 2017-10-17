# Easy implementation

def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                flag = True
                for j in range(1, len(needle)):
                    if i + j > len(haystack) - 1:
                        return -1
                    if needle[j] != haystack[i+j]:
                        flag = False
                        break
                if flag:
                    return i
        return -1
