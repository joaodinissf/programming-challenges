import bisect
import heapq
from typing import List

from furthest_building_you_can_reach_input import large_input, large_input_2


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        reached = 0

        ladders_heap = []
        for ix in range(1, len(heights)):
            delta = heights[ix] - heights[ix - 1]
            if delta > 0:
                if ladders > 0:
                    heapq.heappush(ladders_heap, delta)
                    ladders -= 1
                elif ladders_heap and delta > ladders_heap[0]:
                    bricks -= heapq.heappop(ladders_heap)
                    heapq.heappush(ladders_heap, delta)
                elif bricks >= delta:
                    bricks -= delta
                else:
                    return reached

            if bricks < 0:
                return reached
            reached = ix

        return reached


if __name__ == "__main__":
    s = Solution()
    print(s.furthestBuilding([], 0, 0))  # 0
    print(s.furthestBuilding([1, 5], 0, 0))  # 0
    print(s.furthestBuilding([1, 13, 1, 1, 13, 5, 11, 11], 10, 8))  # 7
    print(s.furthestBuilding([1, 5, 1, 2, 3, 4, 10000], 4, 1))  # 5
    print(s.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))  # 4
    print(s.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))  # 7
    print(s.furthestBuilding([14, 3, 19, 3], 17, 0))  # 3
    print(s.furthestBuilding(large_input, 926413609, 24790))  # 72329
    print(s.furthestBuilding(large_input_2, 33671263, 108))  # 589
