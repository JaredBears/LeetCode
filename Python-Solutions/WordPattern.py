class Solution:
    # The idea is to use a dictionary to map each character in the pattern to a word in the string.
    # We iterate through the pattern and the string and map each character in the pattern to a word
    # in the string. If the character/word is not in the dictionary, we add it to the dictionary with the
    # index of the character/word as the value. If the character/word is in the dictionary, we check if
    # the value of the character/word in the dictionary is equal to the value of the word/character in the
    # dictionary. If the values are not equal, we return False. If the values are equal, we continue to
    # the next character/word in the pattern/string.
    # Time Complexity: O(n) where n is the number of characters in the pattern
    # Space Complexity: O(n)
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_index = {}
        words = s.split()
        N = len(pattern)
        if N != len(words):
            return False
        
        for i in range(N):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)
            
            if char_key not in map_index:
                map_index[char_key] = i
            
            if char_word not in map_index:
                map_index[char_word] = i 
            
            if map_index[char_key] != map_index[char_word]:
                return False
        
        return True