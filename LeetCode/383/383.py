class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    rnDict = {}
    magDict = {}

    for letter in ransomNote:
      if letter in rnDict:
        rnDict[letter] += 1
      else:
        rnDict[letter] = 1

    for letter in magazine:
      if letter in magDict:
        magDict[letter] += 1
      else:
        magDict[letter] = 1
        
    ans = True
    
    for letter in rnDict:
      if letter not in magDict:
        ans = False
        break
      else:
        if magDict[letter] < rnDict[letter]:
          ans = False
          break
      
    return ans