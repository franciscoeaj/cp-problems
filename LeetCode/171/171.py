class Solution:
  def titleToNumber(self, columnTitle: str) -> int:
    alphabet = [
      "A", "B", "C", "D", "E", "F", "G", "H",
      "I", "J", "K", "L", "M", "N", "O", "P",
      "Q", "R", "S", "T", "U", "V", "W", "X",
      "Y", "Z"
    ]
    
    def letterToNumber(letter: str) -> int:
      for i in range(len(alphabet)):
        if letter == alphabet[i]: return i + 1
    
    count, j = 0, 0
    for i in range(len(columnTitle) - 1, -1, -1):
      letter = columnTitle[i]
      count += len(alphabet) ** j * letterToNumber(letter) if j > 0 else letterToNumber(letter)
      j += 1
      
    return count

sol = Solution()
print(sol.titleToNumber(input()))

#FXSHRXW

#(26**6 * 6) + (26**5 * 24) + (26**4 * 19) + (26 * 26 * 26 * 8) + (26 * 26 * 18) + (26 * 24) + 23