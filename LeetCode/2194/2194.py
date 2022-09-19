class Solution:
  def cellsInRange(self, s: str) -> list[str]:
    alphabet = [
      "A", "B", "C", "D", "E", "F", "G", "H",
      "I", "J", "K", "L", "M", "N", "O", "P",
      "Q", "R", "S", "T", "U", "V", "W", "X",
      "Y", "Z"
    ]

    colStart, colEnd = s[0], s[3]
    rowStart, rowEnd = int(s[1]), int(s[4]) + 1

    cells = []
    for i in range(alphabet.index(colStart), alphabet.index(colEnd) + 1):
      for j in range(rowStart, rowEnd):
        cells.append('%s%d' % (alphabet[i], j))

    return cells

sol = Solution()
print(sol.cellsInRange(input()))