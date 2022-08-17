class Solution:
  def uniqueMorseRepresentations(self, words: List[str]) -> int:
    alphabet = {
      "a": ".-",
      "b": "-...",
      "c": "-.-.",
      "d": "-..",
      "e": ".",
      "f": "..-.",
      "g": "--.",
      "h": "....",
      "i": "..",
      "j": ".---",
      "k": "-.-",
      "l": ".-..",
      "m": "--",
      "n": "-.",
      "o": "---",
      "p": ".--.",
      "q": "--.-",
      "r": ".-.",
      "s": "...",
      "t": "-",
      "u": "..-",
      "v": "...-",
      "w": ".--",
      "x": "-..-",
      "y": "-.--",
      "z": "--.."
    }

    unique_words = set()

    for word in words:
      morse_word = ""
      for letter in word:
        morse_word += alphabet[letter]

      unique_words.add(morse_word)
    
    return len(unique_words)