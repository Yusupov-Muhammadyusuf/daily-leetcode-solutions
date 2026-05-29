"""
LeetCode: Contains Duplicate II
Level: Easy 🟢

Description:
Given an integer array nums and an integer k, return true if there are two 
distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Approach: Hash Map (Sliding Window / Tracking Indices)
Time Complexity: O(n) - We iterate through the array elements only once.
Space Complexity: O(n) - A hash map (dictionary) is used to store the last seen indices of elements.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last seen index of each number
        seen = {}

        # Iterate through the array with both index and value
        for i, num in enumerate(nums):
            # If the number is already in the dictionary and the distance between 
            # the current index and the last seen index is less than or equal to k
            if num in seen and i - seen[num] <= k:
                return True
            
            # Update the dictionary with the current index of the number
            seen[num] = i
        
        # If no such pair is found after checking the whole array
        return False
