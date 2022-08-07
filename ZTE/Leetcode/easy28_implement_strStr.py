"""
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
 or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Input: haystack = "hello", needle = "ll"
Output: 2

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

class Solution:
    def strStr(self, haystack, needle):
        n = len(needle)
        m = len(haystack)
        if n == 0:
            return 0
        elif m == 0 or n > m:
            return -1
        else:
            for i in range(m):
                matched = 0
                if needle[0] == haystack[i]:
                    for c in range(n-1):
                        if i + (c+1) == m:
                            return -1
                        elif needle[c+1] == haystack[i + (c+1)]:
                            matched +=1
                    if matched == n-1:
                        return i
            return -1


if __name__ == "__main__":
    s = Solution()
    needle = "ll"
    haystack = "hello"
    print(s.strStr(haystack, needle))
    needle = "bba"
    haystack = "aaaaaa"
    print(s.strStr(haystack, needle))
    needle = "aaa"
    haystack = "aaa"
    print(s.strStr(haystack, needle))
    needle = "issipi"
    haystack = "mississippi"
    print(s.strStr(haystack, needle))
#     "mississippi"
# "issipi"