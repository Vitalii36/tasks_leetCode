'''
Given the head of a singly linked list, reverse the list,
and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            head = prev
        return head

        # def rev(head):
        #     if not head or not head.next:
        #         return (head, head)
        #
        #     newh, tail = rev(head.next)
        #     tail.next = head
        #     tail = head
        #     head.next = None
        #     return (newh, tail)
        #
        # newh, tail = rev(head)
        # return newh
