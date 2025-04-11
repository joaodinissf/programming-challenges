class Solution:
    def __init__(self):
        self.CUT_OFF = 0xF
        # self.CUT_OFF = 0x3FF

    def getSum(self, a: int, b: int) -> int:
        carry = ((a & b) << 1) & self.CUT_OFF
        sum = a ^ b & self.CUT_OFF
        while carry:
            newCarry = ((sum & carry) << 1) & self.CUT_OFF
            sum = sum ^ carry & self.CUT_OFF
            carry = newCarry
        return sum


def main():
    s = Solution()
    # print(s.getSum(1, 2))
    # print(s.getSum(2, 3))
    # print(s.getSum(1, -1))
    print(s.getSum(-1, 1))


if __name__ == "__main__":
    main()
