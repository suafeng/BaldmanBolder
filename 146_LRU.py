# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

# my implementation

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.ht = dict()
        self.ll = []


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.ht:
            return -1
        else:
            self.ll.remove(key)
            self.ll.insert(0, key)
            return self.ht[key]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.ht:
            self.ht[key] = value
            self.ll.remove(key)
            self.ll.insert(0, key)
        else:
            if len(self.ll) == self.cap:
                #evict
                evict_key = self.ll.pop(-1)
                self.ht.pop(evict_key)
            self.ht[key] = value
            self.ll.insert(0, key)

# The bottlenect can lie on the list I use to track the LRU info.

# Here is other's implementation, which is cool indeed

from collections import deque
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = deque()
        self.map = {}
        self.timec = 0

    def fix_queue(self):
        while len(self.map) > self.capacity:
            key, val, time = self.queue.pop()
            val_r, time_r = self.map[key]

            if (val == val_r and time_r == time):
                self.map.pop(key)



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.timec += 1

        if (not key in self.map):
            return -1

        val, _ = self.map[key]
        self.map[key] = (val, self.timec)
        self.queue.appendleft((key, val, self.timec))

        return val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.timec += 1

        self.map[key] = (value, self.timec)
        self.queue.appendleft((key, value, self.timec))

        self.fix_queue()

# Deque is used and no search in the deque is involved. Keep a time stamp,
# and always append to the deque. When put, look fix_queue function, remove
# deque entries or somethings hashtable entries to keep the cache be in its
# capacity. Continuously append to deque prevent the large overhead of search
# in list and pop the entry out.
