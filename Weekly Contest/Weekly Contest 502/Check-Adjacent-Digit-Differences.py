"""
LeetCode: Check if Adjacent Characters Have Difference At Most Two
Level: Easy 🟢

Description:
Given a string s containing digits, check if the absolute difference between 
every pair of adjacent digits is at most 2. Return True if all adjacent digits 
satisfy this condition, otherwise return False.

Approach: Linear Scan
- Traverse the string once using a loop.
- Compare each character at index i with the next character at index i+1.
- If the difference exceeds 2, return False immediately (early return).

Complexity:
- Time Complexity: O(n) — We traverse the string of length n exactly once.
- Space Complexity: O(1) — Constant space is used as we only use a few variables.
"""

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        # Loop through the string up to the second to last character
        for i in range(len(s) - 1):
            # Calculate the absolute difference between adjacent digits
            diff = abs(int(s[i]) - int(s[i+1]))

            # If the difference is greater than 2, condition fails
            if diff > 2:
                return False
            
        # If the loop finishes without returning False, all differences are <= 2
        return True
