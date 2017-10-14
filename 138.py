# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.

# method 1: use a hashtable, the key is the original node, the value is the
# copy. First round, establish the hash table. Second round, assign the next and
# random pointer for the copy nodes. Cornel case: when the next or random
# pointer are null.
def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        curr = head
        table = dict()
        while curr != None:
            table[curr] = RandomListNode(curr.label)
            curr = curr.next
        for k, v in table.items():
            if k.next == None:
                v.next = None
            else:
                v.next = table[k.next]
            if k.random == None:
                v.random = None
            else:
                v.random = table[k.random]
        return table[head]

# method 2, no need for an hash table. Just append the copy node to the next of
# the original node, like if we have 1->2->3, we can do 1->(1)->2->(2)->3->(3)
# then do another iteration to assign the random pointer: curr.next.random =
# curr.random.next. Need to note that when curr.random == null, previous
# equation is not valid, since curr.random == null and have no next. Also, when
# split the two list, can make use a pseudo head! This is an important
# technique.

def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        curr = head
        # first round, construct
        while curr:
            tmp = curr.next
            copy = RandomListNode(curr.label)
            curr.next = copy
            copy.next = tmp
            curr = tmp
        # second round, assign random pointer
        curr = head
        while curr:
            if curr.random == None:
                curr.next.random = None
            else:
                curr.next.random = curr.random.next
            curr = curr.next.next
        # third round, split those copyed nodes from the original list

        curr = head
        tmp_head = RandomListNode(0)
        new_curr = tmp_head
        while curr:
            copy = curr.next
            curr.next = curr.next.next
            curr = curr.next
            new_curr.next = copy
            new_curr = new_curr.next
        return tmp_head.next
