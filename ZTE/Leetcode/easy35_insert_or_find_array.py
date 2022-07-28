"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4

"""

class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        print(nums)
        if not target or n == 0:
            return 0
        elif target == nums[-1]:
            return n
        else:
            stack = []
            mid = n // 2
            if target > nums[mid]:
                return self.searchInsert(nums[mid:], target)
            else:
                return self.searchInsert(nums[:mid], target)



if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,6]
    target = 5
    print(s.searchInsert(nums, target))
