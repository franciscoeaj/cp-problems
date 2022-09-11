from itertools import permutations
class Solution:
  def tictactoe(self, moves: list[list[int]]) -> str:
    aMoves = []
    bMoves = []
    
    possibleWins = [
      ([0,0],[1,1],[2,2]), #diag
      ([0,2],[1,1],[2,0]), #diag contrario
      ([0,0],[0,1],[0,2]), #linha 1
      ([1,0],[1,1],[1,2]), #linha 2
      ([2,0],[2,1],[2,2]), #linha 3
      ([0,0],[1,0],[2,0]), #col 1
      ([0,1],[1,1],[2,1]), #col 2
      ([0,2],[1,2],[2,2])  #col 3
    ]
    
    for i in range(len(moves)):
      if i % 2 == 0:
        aMoves.append(moves[i])
      else:
        bMoves.append(moves[i])
    
    ans = "Pending"

    permsA = permutations(aMoves, 3)
    for permA in permsA:
      if permA in possibleWins:
        ans = "A"
        break

    permsB = permutations(bMoves, 3)
    for permB in permsB:
      if permB in possibleWins:
        ans = "B"
        break
        
    if ans == "Pending" and len(aMoves) == 5 and len(bMoves) == 4:
      ans = "Draw"
      
    return ans

sol = Solution()

#print(sol.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]), "A")
#print(sol.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]), "B")
#print(sol.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]), "Draw")
#print(sol.tictactoe([[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]]), "A")
print(sol.tictactoe([[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]), "B")
#print(sol.tictactoe([[0,0],[1,1]]), "Pending")