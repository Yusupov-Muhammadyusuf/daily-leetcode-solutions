"""
LeetCode: Longest Continuous Monotonic Subarray
Level: Easy 🟢

Description:
Given an array of integers nums, return the length of the longest subarray 
of nums that is either strictly increasing or strictly decreasing.

Approach: Single Pass (Tracking Increments and Decrements)
Time Complexity: O(n) - We iterate through the array elements only once.
Space Complexity: O(1) - Only a few variables are used to keep track of the lengths.
"""

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # If the array is empty, the longest subarray length is 0
        if not nums:
            return 0
            
        max_len = 1
        inc = 1
        dec = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1  # Reset decreasing sequence counter
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1  # Reset increasing sequence counter
            else:
                # If elements are equal, reset both counters
                inc = 1
                dec = 1
            
            # Update the maximum length found so far
            max_len = max(max_len, inc, dec)
        
        return max_len
