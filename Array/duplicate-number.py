"""
LeetCode: Find the Duplicate Number
Level: Medium 🟠

Description:
Given an array of integers 'nums' containing n + 1 integers where each integer 
is in the range [1, n] inclusive. There is only one repeated number in 'nums', 
return this repeated number.

Approach: Hash Set
Time Complexity: O(n) - We iterate through the array once.
Space Complexity: O(n) - In the worst case, we store n unique elements in the set.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Create an empty set to keep track of numbers we have already encountered
        seen = set()

        for num in nums:
            # If the current number is already in the 'seen' set, it is a duplicate
            if num in seen:
                return num
            
            # If it is the first time seeing this number, add it to the set
            seen.add(num)

        # The problem guarantees one duplicate, so we don't need a fallback return
