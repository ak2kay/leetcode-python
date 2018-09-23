#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (42.96%)
# Total Accepted:    409.2K
# Total Submissions: 948.5K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = l1 if l1.val <= l2.val else l2

        if head ==  l1:
            l1 = l1.next
        else:
            l2 = l2.next

        cur = head

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next

        while l1:
           cur.next = l1
           l1 = l1.next
           cur = cur.next

        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return head
