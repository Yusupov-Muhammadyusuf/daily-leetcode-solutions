"""
LeetCode: Palindrome Number
Level: Easy 🟢

Description:
Given an integer x, return true if x is a palindrome, and false otherwise.
An integer is a palindrome when it reads the same forward and backward.
For example, 121 is a palindrome while 123 is not.

Approach: Reversing the Integer
Time Complexity: O(log n) - We iterate through the digits of the number.
Space Complexity: O(1) - Only a few variables are used to store the reversed number.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes (e.g., -121 reversed is 121-)
        if x < 0:
            return False

        original_number = x
        reversed_number = 0

        # Reverse the integer mathematically
        while x > 0:
            last_digit = x % 10
            reversed_number = reversed_number * 10 + last_digit
            x //= 10

        # If the reversed number is equal to the original, it's a palindrome
        return reversed_number == original_number
