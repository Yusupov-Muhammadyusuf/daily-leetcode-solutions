"""
LeetCode: Rotate String
Level: Easy 🟢

Description:
Given two strings s and goal, return true if and only if s can become goal 
after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.

Approach: String Concatenation & Substring Search
Time Complexity: O(n) - Checking if 'goal' is a substring of 's + s' takes linear time.
Space Complexity: O(n) - Creating the concatenated string 's + s' requires extra space.
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If the lengths are not equal, s can never be transformed into goal.
        # If lengths match, concatenating s with itself (s + s) will contain 
        # all possible rotations of the string as substrings.
        return len(s) == len(goal) and goal in (s + s)
