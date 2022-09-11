import math

def isBadVersion(num: int) -> bool:
  return num >= 1702766719

class Solution:  
  def firstBadVersion(self, n: int) -> int:
    memo = {}
    l, r, i = 1, n, 1
    while True:
      candidate = (l + r) // 2

      if (candidate not in memo):
        memo[candidate] = isBadVersion(candidate)
        
      if (candidate - 1 not in memo):
        memo[candidate - 1] = isBadVersion(candidate - 1)
        
      if (candidate + 1 not in memo):
        memo[candidate + 1] = isBadVersion(candidate + 1)
      
      
      prevIsBad, isBad, nextIsBad = memo[candidate - 1], memo[candidate], memo[candidate + 1]

      if candidate == 1 and isBad: return candidate
      
      # candidato atual é versao ruim
      if isBad:
        # se a versao anterior nao for ruim, retorno a atual
        if not prevIsBad: 
          return candidate

        r = candidate - 1
      
      # candidato atual é versao boa
      if not isBad:
        # se a prox versao for ruim, retorno ela
        if nextIsBad: 
          return candidate + 1

        l = candidate + 1

    print(memo)

sol = Solution()
print(sol.firstBadVersion(int(input())))