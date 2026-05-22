"""
LeetCode: Majority Element II
Level: Medium 🟠

Description:
Given an integer array nums, find all elements that appear more than ⌊ n/3 ⌋ times.

Approach: Hash Map (Using Counter)
Time Complexity: O(n) - Iterating through the array to count frequencies takes linear time.
Space Complexity: O(n) - In the worst case, the hash map stores all unique elements of the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number in the array
        counts = Counter(nums)
        
        # Define the threshold requirement (more than n / 3 times)
        threshold = len(nums) / 3
        result = []

        # Iterate through the unique numbers and their counts
        for num, count in counts.items():
            # If the number appears more than the threshold, add it to the result
            if count > threshold:
                result.append(num)
        
        return result
