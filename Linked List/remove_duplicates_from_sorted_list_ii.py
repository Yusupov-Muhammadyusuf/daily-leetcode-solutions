"""
LeetCode: 82. Remove Duplicates from Sorted List II
Level: Medium 🟡

Description:
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Approach: Sentinel Head + Two Pointers
1. We use a dummy (sentinel) node to handle cases where the head itself needs to be removed.
2. We use 'prev' pointer to track the last node in the 'clean' list (without duplicates).
3. We traverse the list with 'head' pointer:
   - If we find a sequence of duplicates, we skip all of them.
   - If no duplicates are found, we move 'prev' forward.

Time Complexity: O(n) - We traverse the list exactly once.
Space Complexity: O(1) - We only use a few constant pointers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Sentinel node points to the head to simplify edge cases
        dummy = ListNode(0, head)
        # 'prev' is the last node that is known to not have any duplicates
        prev = dummy

        while head:
            # If it's a beginning of duplicates range
            if head.next and head.val == head.next.val:
                # Move until the end of the duplicates range
                while head.next and head.val == head.next.val:
                    head = head.next
                
                # Skip all duplicates and connect 'prev' to the node after duplicates
                prev.next = head.next
            else:
                # No duplicates found, move 'prev' pointer forward
                prev = prev.next

            # Move 'head' pointer forward
            head = head.next

        return dummy.next
