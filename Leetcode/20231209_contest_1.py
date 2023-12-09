from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        intersection_counts = []

        val_to_append = 0
        for key in nums1:
            if key in set2:
                val_to_append += 1
        intersection_counts.append(val_to_append)

        val_to_append = 0
        for key in nums2:
            if key in set1:
                val_to_append += 1
        intersection_counts.append(val_to_append)

        return intersection_counts


def main():
    # nums1 = [1, 2, 2, 1]
    nums1 = [4, 3, 2, 3, 1]
    # nums2 = [2, 2]
    nums2 = [2, 2, 5, 2, 3, 6]
    sol = Solution()
    print(sol.findIntersectionValues(nums1, nums2))


if __name__ == "__main__":
    main()
