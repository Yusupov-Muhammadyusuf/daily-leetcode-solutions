"""
LeetCode: Linked List Cycle
Level: Easy 🟢

Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be 
reached again by continuously following the next pointer.

Approach: Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
1. Use two pointers, 'slow' and 'fast'.
2. 'slow' moves one step at a time, while 'fast' moves two steps.
3. If there is a cycle, the 'fast' pointer will eventually meet the 'slow' pointer.
4. If 'fast' reaches the end (None), then there is no cycle.

Time Complexity: O(n) - In the worst case, we visit each node.
Space Complexity: O(1) - We only use two constant pointers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Base case: if list is empty or has only one node, no cycle possible
        if not head or not head.next:
            return False

        # Initialize both pointers at the head
        slow = head
        fast = head

        # Traverse the list
        while fast and fast.next:
            slow = slow.next          # moves 1 step
            fast = fast.next.next     # moves 2 steps

            # If pointers meet, there is a cycle
            if slow == fast:
                return True

        # If fast reaches the end, no cycle exists
        return False
