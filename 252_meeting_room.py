# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
# meetings.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.

# easy one. Sort according to the start time. If next start time smaller than
# current end time, there is a conflict, then return false. If there is no
# such conflict, return true

def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda inter: inter.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True
