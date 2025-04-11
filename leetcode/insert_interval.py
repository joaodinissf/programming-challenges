import bisect
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insertionPos = bisect.bisect(intervals, newInterval)
        intervals.insert(insertionPos, newInterval)

        # Find largest overlap from the interval immediately to the left of insertionPos
        if insertionPos - 1 >= 0 and intervals[insertionPos - 1][1] >= intervals[insertionPos][0]:
            intervals[insertionPos - 1][1] = max(
                intervals[insertionPos - 1][1], intervals[insertionPos][1]
            )
            del intervals[insertionPos]
            insertionPos -= 1

        rightIntervalIx = insertionPos
        while (
            rightIntervalIx + 1 < len(intervals)
            and intervals[insertionPos][1] >= intervals[rightIntervalIx + 1][0]
        ):
            rightIntervalIx += 1

        if rightIntervalIx > insertionPos:
            intervals[insertionPos][1] = max(
                intervals[insertionPos][1], intervals[rightIntervalIx][1]
            )
            del intervals[insertionPos + 1 : rightIntervalIx + 1]

        return intervals


if __name__ == "__main__":
    s = Solution()
    # print(s.insert([[1, 3], [6, 9]], [2, 5]))  # [[1,5],[6,9]]
    # print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # [[1,2],[3,10],[12,16]]
    print(s.insert([[1, 5]], [0, 6]))  # [[1,2],[3,10],[12,16]]
