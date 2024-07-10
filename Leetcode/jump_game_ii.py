import math
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        distance_in_hops = [0] * len(nums)
        for ix in range(len(nums) - 2, -1, -1):
            if nums[ix] > 0:
                distance_in_hops[ix] = 1 + min(
                    distance_in_hops[ix + 1 : ix + nums[ix] + 1], default=0
                )
            else:
                distance_in_hops[ix] = math.inf
        return distance_in_hops[0]


if __name__ == "__main__":
    s = Solution()
    # print(s.jump([2, 3, 1, 1, 4]))  # 2
    # print(s.jump([2, 3, 0, 1, 4]))  # 2
    # print(s.jump([2, 1]))  # 1
    # print(s.jump([0]))  # 0
    print(s.jump([2, 0, 2, 4, 6, 0, 0, 3]))  # 3
