"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Follow up: Could you solve it without converting the integer to a string?
"""

import math as m
import time

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif (x >= 0 and x / 10 < 1):
            return True
        else:
            i = int(m.log10(x)) + 1
            j = int(i / 2) + (i % 2 > 0)
            print(i, j)
            iterC = 0
            while j <= i:
                l = x % 10** j // 10 ** (j-1)
                r = x // 10 ** (i-j) % 10 ** 1
                #print(l, r)
                if l == r:
                    iterC+=1
                else:
                    return False
                j+=1
            if j == i:
                return True
            else:
                return False

    # def ispal(self, x):
    #     i = 0
    #     while 10 ** i < x:

if __name__ == "__main__":
    sol = Solution()
    num = 121
    print(sol.isPalindrome(num))
    num = 10
    print(sol.isPalindrome(num))
    num = 0
    print(sol.isPalindrome(num))
    num = 1
    print(sol.isPalindrome(num))
    num = 99999
    print(sol.isPalindrome(num))
    num = 12321
    print(sol.isPalindrome(num))
    num = 12345654341
    print(sol.isPalindrome(num))