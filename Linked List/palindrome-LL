"""
LeetCode: Palindrome Linked List
Level: Easy 🟢

Description:
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Approach: Two Pointers (Slow & Fast) + In-place Reversal
Time Complexity: O(n) - We traverse the list to find the middle and compare halves.
Space Complexity: O(1) - We modify the list in-place without extra data structures.
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Base case: an empty list or a single node is always a palindrome
        if not head or not head.next:
            return True

        # Phase 1: Find the middle of the linked list
        # 'slow' will end up at the start of the second half
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Phase 2: Reverse the second half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Phase 3: Compare the first half and the reversed second half
        # 'left' starts at the head, 'right' starts at the end of the original list
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
