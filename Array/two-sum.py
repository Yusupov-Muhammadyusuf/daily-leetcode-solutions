"""
LeetCode: Two Sum
Level: Easy 🟢

Description:
Given an array of integers 'nums' and an integer 'target', return indices 
of the two numbers such that they add up to 'target'.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Approach: Brute Force
- Time Complexity: O(n^2) - We use nested loops to check every pair.
- Space Complexity: O(1) - No extra space used except for variables.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        # Outer loop to iterate through each element as the first number
        for i in range(n):
            # Inner loop to check all subsequent elements as the second number
            for j in range(i + 1, n):
                # Check if the sum of the two elements equals the target
                if nums[i] + nums[j] == target:
                    # Return the indices of the two numbers
                    return [i, j]
