# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?

# The idea is extremely simple, using two pointers, one fast one slow,
# the slow one step per move, the fast one two step per move. If there
# is cycle in the linked list, the slow and fast pointers will finally
# meet with each other, then return true. If any of these two points
# becomes null, means there is no cycle, return false.

def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            if fast.next == None:
                break
            else:
                fast = fast.next.next
            if slow == fast:
                return True
        return False
