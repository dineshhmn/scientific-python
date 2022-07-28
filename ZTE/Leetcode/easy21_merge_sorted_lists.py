"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        ret_val = ListNode()
        ptr = ret_val
        while l1 or l2:
            v = 0
            l1v = l1.val if l1 else None
            l2v = l2.val if l2 else None
            if (l1v is not None and l2v is not None):
                if l1v <= l2v:
                    v = l1v
                    l1 = l1.next
                else:
                    v = l2v
                    l2 = l2.next
            elif l1v:
                v = l1v
                l1 = l1.next
            elif l2v:
                v = l2v
                l2 = l2.next
            else:
                return ListNode()
            ptr.val = v
            if (l1 or l2):
                ptr.next = ListNode()
                ptr = ptr.next
        return ret_val

def ll_printer(rt):
    ctr = 0
    while rt:
        ctr += 1
        print(rt.val, ctr)
        rt = rt.next


if __name__ == "__main__":
    s = Solution()
    lst1 = ListNode(0)
    lst2 = ListNode(1)
    lst3 = ListNode(2)
    lst4 = ListNode(3)
    lst5 = ListNode(4)
    lst6 = ListNode(5)
    lst1.next = lst2
    lst2.next = lst3
    lst3.next = lst4
    lst4.next = lst5
    lst5.next = lst6
    ltt1 = ListNode(0)
    ltt2 = ListNode(2)
    ltt3 = ListNode(4)
    ltt4 = ListNode(6)
    ltt5 = ListNode(8)
    ltt6 = ListNode(9)
    ltt1.next = ltt2
    ltt2.next = ltt3
    ltt3.next = ltt4
    ltt4.next = ltt5
    ltt5.next = ltt6
    r = s.mergeTwoLists(lst1, ltt1)
    #ll_printer(r)
    l1 = ListNode(None)
    l2 = ListNode(None)
    r = s.mergeTwoLists(l1, l2)
    ll_printer(r)