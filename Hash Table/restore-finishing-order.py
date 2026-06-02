"""
LeetCode Match: Intersection of Two Arrays / Relative Order
Level: Easy 🟢

Description:
Given an array 'order' representing a sequence and an array 'friends', 
return a new list containing elements from 'order' that exist in 'friends', 
preserving their original relative order.

Approach: Hash Table (Set for O(1) Lookups)
Time Complexity: O(n + m) - Where 'n' is the length of 'order' and 'm' is the length of 'friends'.
Space Complexity: O(m) - To store unique elements of 'friends' in a hash set.
"""

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # Convert friends list to a set for O(1) time complexity lookups
        seen = set(friends)
        finish_order = []

        # Iterate through the order array and filter elements
        for element in order:
            if element in seen:
                finish_order.append(element)
        
        return finish_order
