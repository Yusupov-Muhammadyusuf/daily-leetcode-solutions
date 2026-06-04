"""
LeetCode: Power of Four
Level: Easy 🟢

Description:
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four if there exists an integer x such that n == 4^x.

Approach: Iterative Division (Loop)
Time Complexity: O(log_4 n) - In each step, n is divided by 4, leading to a logarithmic number of iterations.
Space Complexity: O(1) - Only a constant amount of extra space is used.
"""

function isPowerOfFour(n: number): boolean {
    // A power of four must be strictly greater than zero
    if (n <= 0) {
        return false;
    }

    // Keep dividing by 4 as long as the number is divisible by 4
    while (n % 4 === 0) {
        n /= 4;
    }

    // If the remaining number is 1, then the original number was a power of four
    return n === 1;
}
