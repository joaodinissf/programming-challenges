class Solution:
    def hasLetterAdjacent(self, word, ix):
        if ix >= len(word) - 1:
            return False
        return (
            word[ix] == word[ix + 1]
            or chr(ord(word[ix]) + 1) == word[ix + 1]
            or chr(ord(word[ix]) - 1) == word[ix + 1]
        )

    def removeAlmostEqualCharacters(self, word: str) -> int:
        num_changed_characters = 0
        ix = 0
        while ix < len(word) - 1:
            if self.hasLetterAdjacent(word, ix):
                if self.hasLetterAdjacent(word, ix + 1):
                    ix += 1
                num_changed_characters += 1

            ix += 1

        return num_changed_characters


def main():
    word1 = "aaaaa"
    word2 = "abddez"
    word3 = "zyxyxyz"
    sol = Solution()
    print(sol.removeAlmostEqualCharacters(word1))
    print(sol.removeAlmostEqualCharacters(word2))
    print(sol.removeAlmostEqualCharacters(word3))


if __name__ == "__main__":
    main()
