"""
LeetCode: Contains Duplicate
Level: Easy 🟢

Description:
Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

Approach: Hash Set (Using len comparison)
Time Complexity: O(n) - Converting the list to a set takes linear time.
Space Complexity: O(n) - In the worst case, the set stores all elements of the array.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Compare the length of the original list with the length of its unique elements (set).
        # If any elements are duplicated, the set's length will be smaller than the list's length.
        return len(nums) != len(set(nums))
