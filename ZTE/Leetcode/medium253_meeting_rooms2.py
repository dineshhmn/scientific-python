"""Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Input: intervals = [[7,10],[2,4]]
Output: 1
"""

class Solution:
    def minMeetingRooms(self, intervals):
        ints = sorted(intervals, key=lambda x: x[0])
        n = len(ints)
        rms = []
        for i in range(n):
            ctr = 0
            for ky in rms:
                current_max = 0
                pref_index = 0
                index = 0
                if ints[i][0] >= ky[0] and ints[i][0] < ky[1] :
                    ctr +=1
                elif ints[i][0] >= ky[1]:
                    if current_max == 0 or ints[i][0] -  ky[1] > current_max:
                        current_max = ints[i][0] -  ky[1]
                        pref_index = ky
                        break
            if ctr == len(rms):
                rms.append((ints[i][0], ints[i][1]))
            elif pref_index:
                rms.remove(pref_index)
                rms.append((ints[i][0], ints[i][1]))
        return len(rms)

if __name__ == "__main__":
    s = Solution()
    # intervals = [[7,10],[2,4]]
    # print('1. ',s.minMeetingRooms(intervals))
    # intervals = [[0,30],[5,10],[15,20]]
    # print('2. ',s.minMeetingRooms(intervals))
    # intervals = [[9,10],[4,9],[4,17]]
    # print('3. ',s.minMeetingRooms(intervals))
    # intervals = [[1,5],[8,9],[8,9]]
    # print('4. ',s.minMeetingRooms(intervals))
    intervals = [[1,8],[6,20],[9,16],[13,17]]
    print('5. ',s.minMeetingRooms(intervals))
    intervals = [[26,29],[19,26],[19,28],[4,19],[4,25]]
    print('6. ',s.minMeetingRooms(intervals))

