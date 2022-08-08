"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Input: s = "aba"
Output: true

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Input: s = "abc"
Output: false
"""

class Solution:
    def validPalindrome(self, s):
        n = len(s)
        sl = list(s)
        mid = int(n / 2) if n %2 == 0 else int(n/2) + (n%2 > 0)
        ctr = 0
        non_match = []
        l = 0
        r = n-1
        for j in range(1,mid+1):
            if sl[l] == sl[r]:
                l +=1
                r -=1
                ctr +=1
            elif len(non_match) < 2:
                if sl[l+1] == sl[r]:
                    print("one")
                    non_match.append(l)
                    l +=1
                elif s[l] == s[r-1]:
                    print("two")
                    non_match.append(r)
                    r -=1
        #print(non_match)
        if len(non_match) == 1:
            print("Three")
            sl_rt = sl.copy()
            sl.pop(non_match[0])
            s_lt = "".join(sl)
            return self.validPalindrome(s_lt)
        elif ctr == mid:
            return True
        else:
            return False

    def validPalindrome(self, s):
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            if s[left] != s[right]:
                leftstring = s[:left]+s[left+1:]
                rightstring = s[:right]+s[right+1:]
                return leftstring == leftstring[::-1] or rightstring == rightstring[::-1]
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    s = Solution()
    st = "abc"
    print("1.",s.validPalindrome(st))
    st = "aba"
    print("2.",s.validPalindrome(st))
    st = "abca"
    print("3.",s.validPalindrome(st))
    st = "acbca"
    print("4.",s.validPalindrome(st))
    st = "deeee"
    print("5.",s.validPalindrome(st))
    st = "cbbcc"
    print("6.",s.validPalindrome(st))
    st = "cdbeeeabddddbaeedebdc"
    print("7.",s.validPalindrome(st))
    st = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    print("8.",s.validPalindrome(st))
    st = "ebcbbececabbacecbbcbe"
    print("9.",s.validPalindrome(st))