class Solution:
    def isVowel(self, letter: str) -> bool:
        return letter in "aeiouAEIOU"

    def reverseVowels(self, s: str) -> str:
        vowelsIdxs = []

        letters = []
        for i in range(len(s)):
            letters.append(s[i])
            if (self.isVowel(s[i])):
                vowelsIdxs.append((i, s[i]))

        if len(vowelsIdxs) == 1:
            return s

        for i in range(len(vowelsIdxs) // 2):
            head = vowelsIdxs[i]
            tail = vowelsIdxs[-(i + 1)]

            letters[head[0]], letters[tail[0]] = letters[tail[0]], letters[head[0]]
        
        return "".join(letters)