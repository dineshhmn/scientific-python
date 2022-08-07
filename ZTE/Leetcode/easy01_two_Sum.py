"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1 = range(len(nums))
        loopkup_dict = {nums[x]: x for x in l1}
        for x in range(len(nums)):
            if target - nums[x] in loopkup_dict.keys() and loopkup_dict[target - nums[x]] != x:
                return [x, loopkup_dict[target - nums[x]]]


if __name__ == "__main__":
    t = 0
    nums = []
    sol = Solution()

    t = 9
    nums = [2,7,11,15]
    sol.twoSum(nums, t)
    t = 6
    nums = [3,2,4]
    sol.twoSum(nums, t)
    t = 6
    nums = [3,3]
    sol.twoSum(nums, t)
