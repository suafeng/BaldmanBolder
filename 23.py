# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.

# if we have n nodes in total and k lists. If we use the method that each time
# we scan through these k lists and find a minimum to insert to the resulting
# list, time complexity will be O(nk), since to place a node we have to linear
# k lists. Lead to time limit exceeded.
# We can merge two list at a time. Then the time complexity is O(nk/2)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result_head = ListNode(0)
        result = result_head
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        if list1:
            result.next = list1
        if list2:
            result.next = list2
        return result_head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        result = lists.pop(0)
        while lists:
            result = self.mergeTwoLists(result, lists.pop(0))
        return result
