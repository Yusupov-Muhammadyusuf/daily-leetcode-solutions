"""
LeetCode: Word Pattern
Level: Easy 🟢

Description:
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between 
a letter in pattern and a non-empty word in s.

Approach: Hash Map (Two-way Mapping)
Time Complexity: O(N + M) - Where N is the length of pattern and M is the number of words.
Space Complexity: O(W) - Where W is the number of unique words stored in dictionaries.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string into individual words
        words = s.split()

        # If lengths don't match, the pattern cannot be followed
        if len(pattern) != len(words):
            return False

        # Two dictionaries to ensure a bijection (one-to-one mapping)
        char_to_word = {}
        word_to_char = {}

        # Iterate through pairs of characters and words
        for char, word in zip(pattern, words):
            # Check if character is already mapped to a different word
            if char in char_to_word and char_to_word[char] != word:
                return False
            
            # Check if word is already mapped to a different character
            if word in word_to_char and word_to_char[word] != char:
                return False

            # Establish the bidirectional mapping
            char_to_word[char] = word
            word_to_char[word] = char

        return True
