"""
LeetCode: Merge Two Sorted Lists
Level: Easy 🟢

Description:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Approach: Iterative with Dummy Node
Time Complexity: O(n + m) - Where n and m are lengths of the two lists.
Space Complexity: O(1) - We only rearrange existing nodes, no extra memory.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the starting point of the merged list.
        # 'tail' will keep track of the last node in the new list.
        dummy = ListNode()
        tail = dummy

        # 2. Iterate while both lists have nodes remaining.
        while list1 and list2:
            # 3. Compare the values of the current nodes in both lists.
            if list1.val < list2.val:
                # Attach list1's node if it's smaller
                tail.next = list1
                list1 = list1.next  # Move list1 pointer forward
            else:
                # Attach list2's node if it's smaller or equal
                tail.next = list2
                list2 = list2.next  # Move list2 pointer forward
            
            # 4. Move the tail pointer forward to the newly added node.
            tail = tail.next
            
        # 5. If one list is exhausted, attach the remainder of the other list.
        # Since the input lists are already sorted, we just link the rest.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # 6. Return dummy.next, which is the head of the merged sorted list.
        return dummy.next
