"""
LeetCode: Concatenate Array with Its Reverse
Level: Easy 🟢

Description:
Given an array of integers `nums`, create a new array that is the concatenation 
of the original array and its reversed version.

Approach: Array Concatenation and Slicing
- Use Python's slicing technique `nums[::-1]` to create a reversed copy of the array.
- Concatenate the original `nums` array with the reversed array using the `+` operator.
- Return the resulting combined array.

Complexity:
- Time Complexity: O(n) — Creating a reversed copy takes O(n) time, and concatenating 
  two arrays of size n takes O(n) time, where n is the length of `nums`.
- Space Complexity: O(n) — The algorithm creates a new array of size 2n to store 
  the result. Extra memory is directly proportional to the input size.
"""

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        # nums[::-1] filters the list in reverse order, 
        # then + operator joins the original list with the reversed list
        return nums + nums[::-1]
