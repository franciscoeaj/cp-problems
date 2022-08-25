class Solution:
  def firstUniqChar(self, s: str) -> int:
    charsCount = {}

    for letter in s:
      if letter in charsCount:
        charsCount[letter] += 1
      else:
        charsCount[letter] = 1
    
    print(charsCount)
    
    ans = -1
    for char in charsCount:
      if charsCount[char] == 1:
        for i in range(len(s)):
          if s[i] == char:
            ans = i
            break
        break
            
    return ans