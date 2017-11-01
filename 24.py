# Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# the key idea is to keep a prev pointer.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        curr = head
        new_head = curr.next
        if new_head == None:
            return head
        prev = None
        while curr != None:
            if curr.next == None:
                break
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = curr
            if prev:
                prev.next = tmp
            prev = curr
            curr = curr.next
        return new_head
