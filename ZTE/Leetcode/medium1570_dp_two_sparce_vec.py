"""
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
"""

class SparseVecto
    def __init__(self, nums):
        self.nums = self.make_dict(nums)

    def make_dict(self, lst):
        return {i:x for i, x in enumerate(lst) if x > 0}

    def dotProduct(self, vec: 'SparseVector'):
        return sum([self.nums[x] * vec.nums[x] for x in self.nums.keys() if x in vec.nums.keys()])

    # # Return the dotProduct of two sparse vectors
    # def dotProduct2(self, vec: 'SparseVector'):
    #     n1 = len(self.nums)
    #     n2 = len(vec.nums)
    #     mx = min(n1, n2)
    #     summ = 0
    #     #print(n1, n2)
    #     for j in range(mx):
    #         #print('minus')
    #         if j >= n1:
    #             #print("zero")
    #             summ += sum(vec.nums[j:])
    #             break
    #         elif j >= n2:
    #             #print("One")
    #             summ += sum(self.nums[j:])
    #             break
    #         elif self.nums[j] > 0 and vec.nums[j] > 0:
    #             #print("two")
    #             summ += self.nums[j] * vec.nums[j]
    #     return summ


if __name__ == "__main__":
    nums1 = [1,0,0,2,3]
    nums2 = [0,3,0,4,0]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    print(v1.dotProduct(v2))
    nums1 = [0,1,0,0,0]
    nums2 = [0,0,0,0,2]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    print(v1.dotProduct(v2))
    nums1 = [0,1,0,0,2,0,0]
    nums2 = [1,0,0,0,3,0,4]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    print(v1.dotProduct(v2))