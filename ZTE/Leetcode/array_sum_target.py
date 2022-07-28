"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Only one valid answer exists.

# Solution
Runtime: 66 ms, faster than 90.94% of Python3 online submissions for Two Sum.
Memory Usage: 15.1 MB, less than 50.08% of Python3 online submissions for Two Sum.

"""


import time
class Solution:
    def twoSum(self, nums, target):
        loopkup_dict = {}
        for i, x in enumerate(nums):
            if target - x in loopkup_dict.keys():
                return [loopkup_dict[target - x], i]
            else:
                loopkup_dict[x] = i


if __name__ == "__main__":
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    t1 = time.perf_counter_ns()
    print(s.twoSum(nums, target))
    t2 = time.perf_counter_ns()
    print(int((t2-t1))/100, "microseconds")
    nums = [3,3]
    target = 6
    print(s.twoSum(nums, target))
    nums = [3,2,4]
    print(s.twoSum(nums, target))
    nums = [0,4,3,0]
    target = 0
    print(s.twoSum(nums, target))