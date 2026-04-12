"""
LeetCode: Valid Parentheses
Level: Easy 🟢

Description:
Given a string 's' containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Approach: Stack (LIFO)
Time Complexity: O(n) - We iterate through the string exactly once.
Space Complexity: O(n) - In the worst case (e.g., "((((("), we store all characters in the stack.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        brackets = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in brackets:
                # Pop the top element from stack if it's not empty, else use a dummy value
                top_element = stack.pop() if stack else "#"

                # If the popped element doesn't match the required opening bracket
                if brackets[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack
