"""
LeetCode: Valid Anagram
Level: Easy 🟢

Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Approach: Sorting
Time Complexity: O(n log n) - Where n is the length of the string due to sorting.
Space Complexity: O(n) - To store the sorted copies of the strings.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
            
        # If sorted strings are identical, they are anagrams
        return sorted(s) == sorted(t)
