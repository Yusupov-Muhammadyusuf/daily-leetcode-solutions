"""
LeetCode: Find the Duplicate Number
Level: Medium 🟡

Description:
Given an array of integers nums containing n + 1 integers where each integer 
is in the range [1, n] inclusive. There is only one repeated number in nums, 
return this repeated number.

Approach: Using a Hash Set
Time Complexity: O(n) - We traverse the array once.
Space Complexity: O(n) - In the worst case, we store n-1 elements in the set.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize a set to keep track of numbers we've already encountered
        seen = set()

        for num in nums:
            # If the current number is already in the set, it's the duplicate
            if num in seen:
                return num
            
            # Otherwise, add the number to the set and continue
            seen.add(num)

        # According to the problem constraints, a duplicate always exists
        return -1
