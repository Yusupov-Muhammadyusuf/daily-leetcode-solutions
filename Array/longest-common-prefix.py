"""
LeetCode: Longest Common Prefix
Level: Easy 🟢

Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Approach: Vertical Scanning
Time Complexity: O(S) - where S is the sum of all characters in all strings.
Space Complexity: O(1) - only constant extra space used.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Check if the input list is empty
        if not strs:
            return ""

        # Iterate through each character of the first string (the reference)
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Compare this character with the same position in all other strings
            for j in range(1, len(strs)):
                # If current index 'i' reaches the end of the string strs[j]
                # OR characters do not match, return the prefix found so far
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
            
        # If the loop completes, the entire first string is the common prefix
        return strs[0]
