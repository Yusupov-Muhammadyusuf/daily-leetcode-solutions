"""
LeetCode: Power of Two
Level: Easy 🟢

Description:
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two if there exists an integer x such that n == 2^x.

Approach: Iterative Division (Loop)
Time Complexity: O(log n) - In each step, n is divided by 2, leading to a logarithmic number of iterations.
Space Complexity: O(1) - Only a constant amount of extra space is used.
"""

function isPowerOfTwo(n: number): boolean {
    // A power of two must be strictly greater than zero
    if (n <= 0) {
        return false;
    }

    // Keep dividing by 2 as long as the number is even
    while (n % 2 === 0) {
        n /= 2;
    }

    // If the remaining number is 1, then the original number was a power of two
    return n === 1;
}
