"""
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring2(self, s):
        """ Does not work for dvdf test case, trying sol2"""
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            char_dict = {}
            current_len = 0
            i = 0
            while i < n:
                if s[i] not in char_dict.keys():
                    char_dict[s[i]] = i
                elif s[i] in char_dict.keys():
                    if len(char_dict.keys()) > current_len:
                        current_len = len(char_dict.keys())
                        char_dict = {}
                        char_dict[s[i]] = i
                i+=1
            current_len = current_len if current_len > len(char_dict.keys()) else len(char_dict.keys())
        return current_len

    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n <= 1:
            return n
        else:
            st = 0
            en = 1
            current_len = 0
            while en < n:
                if s[en] in s[st:en]:
                    st +=1
                else:
                    en +=1
                t = en - st
                if current_len < t:
                    current_len = t
            return current_len

    def lengthOfLongestSubstring3(self, s):
        """Try #3 with sliding window technique """
        res = 0
        l = 0
        charset = {}
        for r in range(len(s)):
            while s[r] in charset:
                charset.pop(s[l])
                l+=1
            charset[s[r]] = 1
            res = max(res, r - l+1)
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))
    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))
    s = "bbbbb"
    print(sol.lengthOfLongestSubstring(s))
    s = " "
    print(sol.lengthOfLongestSubstring(s))
    s = "au"
    print(sol.lengthOfLongestSubstring(s))
    s = "aab"
    print(sol.lengthOfLongestSubstring(s))
    s = "dvdf"
    print(sol.lengthOfLongestSubstring(s))