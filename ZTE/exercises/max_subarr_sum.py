"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

class Solution:
    def maxSubArray(self, nums):
        """
        Sort Array, taking the largest as peaks and lowest as valley, find sum of chunks between peaks and valleys
        [.., peak, .. . peak, .., valley, .... , peak, valley]
        """
        nums2 = nums.copy()
        nums2.sort()
        va = nums2[0]
        pe = nums2[-1]
        num_chunks = 0
        #if va
        max_sum = [0]
        i = 0
        for x in nums:
            if (x > va and x <= pe):
                max_sum[i]+=x
            else:
                max_sum[i]+=x
                i += 1
                max_sum.append(0)
        return max_sum

    def maxSubArray2(self, nums):
        maxResult = currSum = nums[0]
        for num in nums[1:]:
            currSum = max(currSum+num, num)
            maxResult= max(maxResult,currSum)
        return maxResult


if __name__ == "__main__":
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))
    nums = [1]
    print(s.maxSubArray(nums))
    nums = [5,4,-1,7,8]
    print(s.maxSubArray(nums))