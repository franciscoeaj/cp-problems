class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            largestWord = word1
        elif len(word1) < len(word2):
            largestWord = word2

        res = ""
        i, j = 0, 0
        while len(res) < len(word1) + len(word2):
            if len(word1) != len(word2):
                if i >= len(word1):
                    res += largestWord[j:]
                    break
                if j >= len(word2):
                    res += largestWord[i:]
                    break

            if i == j:
                res += word1[i]
                i += 1
            elif i > j:
                res += word2[j]
                j += 1

        return res