from typing import List


class Solution:
    def getHeightForContainers(self, height: List[int], left: int, right: int) -> int:
        return min(height[left], height[right]) * (right - left)

    def maxArea(self, height: List[int]) -> int:
        largestArea = 0
        endpointsToTry = set([(0, len(height) - 1)])

        while endpointsToTry:
            print(endpointsToTry)
            left, right = endpointsToTry.pop()

            largestArea = max(largestArea, self.getHeightForContainers(height, left, right))

            if height[left] <= height[right]:
                newLeft = left + 1
                while newLeft < right and height[newLeft] <= height[left]:
                    newLeft += 1
                if newLeft < right and height[newLeft] > height[left]:
                    endpointsToTry.add((newLeft, right))

            if height[left] >= height[right]:
                newRight = right - 1
                while left < newRight and height[newRight] <= height[right]:
                    newRight -= 1
                if left < newRight and height[newRight] > height[right]:
                    endpointsToTry.add((left, newRight))

        return largestArea


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([6, 4, 3, 1, 4, 6, 99, 62, 1, 2, 6]))  # 62
