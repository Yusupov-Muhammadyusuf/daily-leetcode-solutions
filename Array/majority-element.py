"""
LeetCode: Majority Element
Level: Easy 🟢

Description:
Given an array 'nums' of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Approach: Hash Map (Dictionary) Counting
Time Complexity: O(n) - We iterate through the list once.
Space Complexity: O(n) - In the worst case, the dictionary stores up to n elements.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Dictionary to store the frequency (count) of each element
        count = {}
        
        # Threshold required to be the majority element (n/2)
        half = len(nums) / 2

        for n in nums:
            # Increment the count of 'n' in the dictionary.
            # If 'n' is not present, .get(n, 0) returns 0, then we add 1.
            count[n] = count.get(n, 0) + 1

            # Check at each step: if the current element's count exceeds n/2,
            # we have found the answer and return it immediately.
            if count[n] > half:
                return n
