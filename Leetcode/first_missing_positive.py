import heapq
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x > 0, nums))
        heapq.heapify(nums)
        i = 1
        while nums:
            next_seen = heapq.heappop(nums)
            if i > next_seen:
                continue
            elif i < next_seen:
                return i
            i += 1
        return i


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))  # 3
    print(s.firstMissingPositive([3, 4, -1, 1]))  # 2
