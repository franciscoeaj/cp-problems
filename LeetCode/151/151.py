class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        revWords = []
        for i in range(len(words) - 1, -1, -1):
            revWords.append(words[i])

        return " ".join(revWords)