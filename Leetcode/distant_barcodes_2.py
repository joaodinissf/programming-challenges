from collections import Counter
from typing import List


class Solution:
    def ix_to_barcode_ix(self, ix, len_barcodes):
        if ix < len_barcodes:
            return ix
        else:
            return ix % len_barcodes - (len_barcodes % 2) + 1

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcode_counter = Counter(barcodes)

        curr_ix = 0
        while barcode_counter:
            value, count = barcode_counter.most_common(1)[0]
            next_ix = curr_ix + 2 * count
            ixs = range(curr_ix, next_ix, 2)
            for ix in ixs:
                barcodes[self.ix_to_barcode_ix(ix, len(barcodes))] = value
            curr_ix = next_ix

            del barcode_counter[value]

        return barcodes


if __name__ == "__main__":
    s = Solution()
    print(s.rearrangeBarcodes([1, 1, 2]))  # [1,2,1]
    print(s.rearrangeBarcodes([1, 1, 2, 2]))  # [1,2,1,2]
    print(s.rearrangeBarcodes([1, 1, 1, 2, 2, 2]))  # [2,1,2,1,2,1]\
    print(s.rearrangeBarcodes([2, 2, 1, 3]))  # [2,3,2,1]
