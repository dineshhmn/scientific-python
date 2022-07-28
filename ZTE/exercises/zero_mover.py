"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
        return nums

if __name__ == "__main__":
    s = Solution()
    nums = [0,1,0,3,12]
    print(s.moveZeroes(nums))
    nums = [0,0,1]
    print(s.moveZeroes(nums))
    nums = [0,0,1,0,2,4,5,6,7,8]
    print(s.moveZeroes(nums))