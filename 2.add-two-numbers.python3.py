#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (29.12%)
# Total Accepted:    584.7K
# Total Submissions: 2M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#
# Definition for singly-linked list.


# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.get_processed(l1)
        l2 = self.get_processed(l2)
        l3 = str(int(l1) + int(l2))[::-1]
        l3 = list(map(int, list(l3)))

        head = self.create_linkedlist(l3)

        return head

    def get_processed(self, ll):
        """convert linklist to a string"""

        res = []
        while ll is not None:
            res.append(ll.val)
            ll = ll.next
        return ''.join(map(str, res[::-1]))

    def create_linkedlist(self, seq):
        """Covert a sequence to a linkedlist.

        The input can be any sequence.
        """

        head = ListNode(seq[0])
        p1 = head
        for i in range(1, len(seq)):
            next_node = ListNode(seq[i])
            p1.next = next_node
            p1 = next_node

        return head


# def print_linklist(head):
#    while head:
#        print(head.val, end=' ')
#    print('')
#
#
# if __name__ == "__main__":
#    l1 = [2, 4, 3]
#    l2 = [5, 6, 4]
#    ex = Solution()
#    l1 = ex.create_linkedlist(l1)
#    print(l1)
#    l2 = ex.create_linkedlist(l2)
#    print(l2)
#    head = ex.addTwoNumbers(l1, l2)
#    print(head)
