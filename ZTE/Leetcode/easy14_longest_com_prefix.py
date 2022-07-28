"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

To make this faster, can I pass a sorted array?
"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        n = len(strs)
        if n == 0:
            return ""
        elif n == 1:
            return strs[0]
        prefix = ""
        for ch in range(len(strs[0])):
            p = 0
            for j in range(1, len(strs)):
                if ch >= len(strs[j]):
                    break
                elif strs[j][ch] == strs[0][ch]:
                    p +=1
            if p + 1 == n and len(prefix) == ch:
                prefix = prefix + strs[0][ch]
        return prefix



if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
    print(s.longestCommonPrefix(["ab","a"]))
    print(s.longestCommonPrefix(["cir","car"]))
    print(s.longestCommonPrefix(["flower","flower","flower","flower"]))