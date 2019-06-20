#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (49.09%)
# Total Accepted:    604.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        p2 = head.next
        head.next = None
        p1 = head
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1

