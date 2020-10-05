'''You are given two non - empty
linked lists representing two
non - negative integers.The digits
are stored in reverse order, and each
of their nodes contains a single
digit.Add the two numbers and
return the sum as a linked list.

You may assume the two
numbers do not contain any
leading zero, except the
number 0  itself.

Example
1:

Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807.
Example
2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example
3:

Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
Output: [8, 9, 9, 9, 0, 0, 0, 1]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def revers_to_int(ls):
            s = ''
            for i in ls:
                s = str(i) + s
            return int(s)

        s = ListNode()
        s.val = l1.val
        for i in range(3):
            r = l1.next.val
            s.val.next = i

        return s  # revers_to_int(l1) + revers_to_int(l1)