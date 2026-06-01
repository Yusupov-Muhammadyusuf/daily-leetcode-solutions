"""
LeetCode: Intersection of Two Arrays
Level: Easy 🟢

Description:
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Approach: Set Intersection (Using & operator)
- Time Complexity: O(n + m) -> Converting lists to sets takes O(n + m) time, 
  and finding the intersection takes O(min(n, m)) on average.
- Space Complexity: O(n + m) -> In the worst case, sets store all elements of both arrays.

How it works:
1. set(nums1) and set(nums2) — Convert both lists into sets to remove duplicate values.
2. set(nums1) & set(nums2) — The '&' operator performs a set intersection, 
   keeping only the elements that exist in BOTH sets.
3. list(...) — Converts the resulting set back into a list format as required by the problem.
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Find common unique elements using the set intersection operator (&)
        return list(set(nums1) & set(nums2))
