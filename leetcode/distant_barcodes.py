from collections import Counter
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcodes = Counter(barcodes)

        new_barcodes = [barcodes.most_common(1)[0][0]]
        barcodes[new_barcodes[-1]] -= 1
        if barcodes[new_barcodes[-1]] == 0:
            del barcodes[new_barcodes[-1]]
        while barcodes:
            if barcodes.most_common(1)[0][0] != new_barcodes[-1]:
                new_barcodes.append(barcodes.most_common(1)[0][0])
                barcodes.update({barcodes.most_common(1)[0][0]: -1})
                if barcodes[new_barcodes[-1]] == 0:
                    del barcodes[new_barcodes[-1]]
            else:
                new_barcodes.append(barcodes.most_common(2)[1][0])
                barcodes.update({barcodes.most_common(2)[1][0]: -1})
                if barcodes[new_barcodes[-1]] == 0:
                    del barcodes[new_barcodes[-1]]

        return new_barcodes


if __name__ == "__main__":
    s = Solution()
    print(s.rearrangeBarcodes([1, 1, 1, 2, 2, 2]))  # [2,1,2,1,2,1]\
    print(s.rearrangeBarcodes([2, 2, 1, 3]))  # [2,3,2,1]
