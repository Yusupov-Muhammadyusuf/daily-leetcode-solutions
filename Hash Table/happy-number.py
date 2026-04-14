"""
LeetCode: Happy Number
Level: Easy 🟢

Description:
Write an algorithm to determine if a number n is happy.
A happy number is a number which eventually reaches 1 when replaced by the sum 
of the squares of its digits. If it enters a cycle that does not include 1, 
it is not a happy number.

Approach: Hash Set (Detecting Cycles)
Time Complexity: O(log n) - The number of digits decreases rapidly.
Space Complexity: O(log n) - To store the numbers seen in the sequence.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # Set to keep track of numbers we have already seen to detect cycles
        seen = set()

        # Continue the process until n becomes 1 (happy) or we hit a cycle
        while n != 1 and n not in seen:
            seen.add(n)
            total_sum = 0

            # Calculate the sum of the squares of the digits
            while n > 0:
                digit = n % 10
                total_sum += digit ** 2
                n //= 10

            # Update n with the calculated sum for the next iteration
            n = total_sum

        # If we exited because n == 1, it's a happy number
        return n == 1
