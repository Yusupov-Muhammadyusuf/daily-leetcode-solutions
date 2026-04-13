"""
LeetCode: Length of Last Word
Level: Easy 🟢

Description:
Given a string 's' consisting of words and spaces, return the length of the 
last word in the string. A word is a maximal substring consisting of non-space 
characters only.

Approach: String Manipulation
Time Complexity: O(n) - We traverse the string to strip and split.
Space Complexity: O(n) - The split method creates a list of words.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Remove leading/trailing whitespace using strip()
        # Step 2: Split the string into a list of words based on spaces
        words = s.strip().split()

        # If the list is not empty, return the length of the last element [-1]
        # Otherwise, return 0 as a fallback
        return len(words[-1]) if words else 0
