# Prob statement: given 2 sorted linked lists, create a sorted linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        ret_val = ListNode()
        if not (l1 and l2):
            print("Bad inputs")
        elif l1:
            return l2
        elif l2:
            return l1
        else:
            while l1 or l2:
                if not l1.val:
                    while l2:
                        ret_val.next = l2
                        l2 = l2.next
                elif not l2.val:
                    while l1:
                        ret_val.next = l1
                        l1 = l1.next
                elif l1.val < l2.val:
                    if not ret_val.val:
                        ret_val = l1
                    else:
                        ret_val.next = l1
                    l1 = l1.next
                elif l1.val > l2.val:
                    if not ret_val.val:
                        ret_val = l1
                    else:
                        ret_val.next = l2
                    l2 = l2.next
                else:
                    if not ret_val.val:
                        ret_val = l1
                    else:
                        ret_val.next = l2
                        ret_val.next = l1
                    l2 = l2.next
                    l1 = l1.next
        return ret_val

if __name__ == "__main__":
    a = ListNode(4)
    z = ListNode(3, a)
    y = ListNode(2, z)
    x = ListNode(1, y)

    s = ListNode(16)
    r = ListNode(8, s)
    q = ListNode(4, r)
    p = ListNode(2, q)
    s = Solution()

    print(s.mergeTwoLists(x, p))


