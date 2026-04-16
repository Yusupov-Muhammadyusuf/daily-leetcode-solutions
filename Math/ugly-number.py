"""
LeetCode: Ugly Number
Level: Easy 🟢

Description:
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Approach: Iterative Division (Prime Factorization)
Time Complexity: O(log n) - The number is divided by 2, 3, or 5 in each step.
Space Complexity: O(1) - Only a constant amount of extra space is used.
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers must be positive
        if n <= 0:
            return False

        # Divide n by each allowed prime factor (2, 3, 5) as much as possible
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        # If the remaining number is 1, it means all factors were 2, 3, or 5
        return n == 1
