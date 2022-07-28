"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""
import time
class Solution:
    def findMedianSortedArrays2(self, nums1, nums2):
        """ Calculates the solution but slow as hell, O(m+n) complexity
            requirement is to create O(log(m+n))
        """
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0
        final = []
        while (i + j +1) < (n1 + n2):
            obj1 = nums1[i] if i < n1 else None
            obj2 = nums2[j] if j < n2 else None
            if (obj1 and obj2):
                if obj1 < obj2:
                    final.append(obj1)
                    obj1 = None
                    i+=1
                else:
                    final.append(obj2)
                    obj2 = None
                    j+=1
            elif obj1:
                final.append(obj1)
            elif obj2:
                final.append(obj2)
        if obj1:
            final.append(obj1)
        elif obj2:
            final.append(obj2)
        n = len(final)
        if i % 2 == 0:
            l = final[int((n/2)-1)]
            r = final[int(n/2)]
            return (l+r)/2
        else:
            return final[int(n/2)]

    def findMedianSortedArrays(self, nums1, nums2):
        """ Calculates the solution but slow as hell, O(m+n) complexity
            requirement is to create O(log(m+n))
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if not (n1 or n2):
            return 0
        elif not n1:
            if n2 % 2 == 0:
                return (nums2[int(n2/2) -1] + nums2[int(n2/2)])/2
            else:
                x = int(n2 / 2) + (n2 % 2 > 0)
                return nums2[x-1]

        elif not n2:
            if n1 % 2 == 0:
                return (nums1[int(n1/2) -1] + nums1[int(n1/2)])/2
            else:
                x = int(n1 / 2) + (n1 % 2 > 0)
                return nums1[x-1]
        else:
            i = 0
            j = 0
            final = []
            obj1 = None
            obj2 = None
            final_len = int((n1 + n2)/2)
            while (i + j) < (final_len):
                obj1 = nums1[i] if i < n1 else None
                obj2 = nums2[j] if j < n2 else None
                if (obj1 is not None and obj2 is not None):
                    if obj1 <= obj2:
                        final.append(obj1)
                        obj1 = None
                        i+=1
                    elif obj2 < obj1:
                        final.append(obj2)
                        obj2 = None
                        j+=1
                if :
                    final.append(obj1)
                elif obj2:
                    final.append(obj2)
            n = len(final)
            print(final)
            if final_len % 2 == 0:
                l = final[-1]
                r = final[-2]
                if l+r:
                    return (l+r)/2.0
                else: return 0
            else:
                return final[-1]


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    t1 = time.perf_counter_ns()
    print(sol.findMedianSortedArrays(nums1, nums2))
    t2 = time.perf_counter_ns()
    print(int((t2-t1))/1000, "microseconds")
    nums1 = [1,3]
    nums2 = [2,7]
    t3 = time.perf_counter_ns()
    print(sol.findMedianSortedArrays(nums1, nums2))
    t4 = time.perf_counter_ns()
    print(int((t4-t3))/1000, "microseconds")
    nums1 = [0,0]
    nums2 = [0,0]
    t5 = time.perf_counter_ns()
    print(sol.findMedianSortedArrays(nums1, nums2))
    t6 = time.perf_counter_ns()
    print(int((t6-t5))/1000, "microseconds")
    nums1 = [3]
    nums2 = [-2,-1]
    t7 = time.perf_counter_ns()
    print(sol.findMedianSortedArrays(nums1, nums2))
    t8 = time.perf_counter_ns()
    print(int((t8-t7))/1000, "microseconds")
    nums1 = [0,0,0,0,0]
    nums2 = [-1,0,0,0,0,0,1]
    t7 = time.perf_counter_ns()
    print(sol.findMedianSortedArrays(nums1, nums2))
    t8 = time.perf_counter_ns()
    nums1 = [1]
    nums2 = [3,4]
    t1 = time.perf_counter_ns()
    print(sol.findMedianSortedArrays(nums1, nums2))
    t2 = time.perf_counter_ns()
    print(int((t2-t1))/1000, "microseconds")