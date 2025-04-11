# Not completed

from typing import List


class Solution:
    def getBranchesThatMustClose(self, n, maxDistance, roads):
        branches_that_must_close = []
        for branch in range(n):
            branch_must_close = True
            for road in roads:
                if branch in [road[0], road[1]] and road[2] <= maxDistance:
                    branch_must_close = False
                    break
            if branch_must_close:
                branches_that_must_close.append(branch)
        return branches_that_must_close

    def getRoadsAfterClosingMandatoryBranches(self, branches_that_must_close, roads):
        return [
            road
            for road in roads
            if road[0] not in branches_that_must_close and road[1] not in branches_that_must_close
        ]

    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        branches_that_must_close = self.getBranchesThatMustClose(n, maxDistance, roads)
        roads_after_closing_mandatory_branches = self.getRoadsAfterClosingMandatoryBranches(
            branches_that_must_close, roads
        )
        return roads_after_closing_mandatory_branches


def main():
    n1 = 3
    maxDistance1 = 5
    roads1 = [[0, 1, 2], [1, 2, 10], [0, 2, 10]]
    n2 = 3
    maxDistance2 = 5
    roads2 = [[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]

    sol = Solution()
    print(sol.numberOfSets(n1, maxDistance1, roads1))
    print(sol.numberOfSets(n2, maxDistance2, roads2))


if __name__ == "__main__":
    main()
