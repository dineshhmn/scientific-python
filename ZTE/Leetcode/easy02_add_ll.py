"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
import time

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        ret_val = ListNode()
        ptr = ret_val
        carry = 0
        while l1 or l2 or carry:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            sum = l1v + l2v + carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            carry = 0
            if sum > 9:
                sum = sum % 10
                carry = 1
            ptr.next = ListNode(sum)
            ptr = ptr.next
        return ret_val.next

def ll_printer(rt):
    ctr = 0
    while rt:
        ctr += 1
        print(rt.val, ctr)
        rt = rt.next


if __name__ == "__main__":
    ls1 = ListNode(2)
    ls2 = ListNode(4)
    ls1.next = ls2
    ls3 = ListNode(3)
    ls2.next = ls3
    lt1 = ListNode(5)
    lt2 = ListNode(6)
    lt1.next = lt2
    lt3 = ListNode(4)
    lt2.next = lt3
    sol = Solution()
    t1 = time.perf_counter_ns()
    ln = sol.addTwoNumbers(ls1, lt1)
    t2 = time.perf_counter_ns()
    print(int((t2-t1))/100, "microseconds")
    #print(ar)
    ll_printer(ln)
    # ls1 = ListNode(0)
    # lt1 = ListNode(0)
    # ln = sol.addTwoNumbers(ls1, lt1)
    # ll_printer(ln)
    # ls1 = ListNode(9)
    # ls2 = ListNode(9)
    # ls1.next = ls2
    # ls3 = ListNode(9)
    # ls2.next = ls3
    # ls4 = ListNode(9)
    # ls3.next = ls4
    # ls5 = ListNode(9)
    # ls4.next = ls5
    # ls6 = ListNode(9)
    # ls5.next = ls6
    # ls7 = ListNode(9)
    # ls6.next = ls7
    # lt1 = ListNode(9)
    # lt2 = ListNode(9)
    # lt1.next = lt2
    # lt3 = ListNode(9)
    # lt2.next = lt3
    # lt4 = ListNode(9)
    # lt3.next = lt4
    # ln = sol.addTwoNumbers(ls1, lt1)
    # ll_printer(ln)

