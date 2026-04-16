"""
LeetCode: Power of Three
Level: Easy 🟢

Description:
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three if there exists an integer x such that n == 3^x.

Approach: Iterative Division
Time Complexity: O(log3 n) - The number is divided by 3 in each iteration.
Space Complexity: O(1) - Only a constant amount of extra space is used.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Negative numbers and zero cannot be powers of three
        if n <= 0:
            return False

        # Continuously divide n by 3 as long as it is divisible
        while n % 3 == 0:
            n //= 3
        
        # If the remaining value is 1, then the original n was a power of three
        return n == 1
