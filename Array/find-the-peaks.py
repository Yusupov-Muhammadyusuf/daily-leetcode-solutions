"""
LeetCode: Find Peaks
Level: Easy 🟢

Description:
Given a 0-indexed integer array 'mountain', find all the peaks in the mountain. 
A peak is defined as an element that is strictly greater than its neighboring 
elements (both the left and right neighbors). Return an array of the indices of 
these peaks in any order. The first and last elements cannot be peaks.

Approach: Linear Scan (Neighbor Comparison)
Time Complexity: O(N) - We iterate through the array 'mountain' exactly once.
Space Complexity: O(1) - Excluding the output list, no extra space is used.
"""

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        result = []

        # Start from index 1 and stop at the second to last index
        # because the first and last elements can never be peaks
        for idx in range(1, len(mountain) - 1):
            
            # Check if the current element is strictly greater than both neighbors
            if mountain[idx] > mountain[idx - 1] and mountain[idx] > mountain[idx + 1]:
                result.append(idx)
        
        return result
