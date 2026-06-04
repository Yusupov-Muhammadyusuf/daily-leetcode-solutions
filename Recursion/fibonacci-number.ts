"""
LeetCode: Fibonacci Number
Level: Easy 🟢

Description:
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
Fibonacci sequence, such that each number is the sum of the two preceding 
ones, starting from 0 and 1.

Approach: Recursion
Time Complexity: O(2^n) - Each call branches into two more calls, leading to exponential growth.
Space Complexity: O(n) - The max depth of the recursion tree determines the call stack space.
"""

function fib(n: number): number {
    // Base cases: if n is 0 or 1, return n
    if (n === 0 || n === 1) {
        return n;
    }

    // Recursive relation: F(n) = F(n-1) + F(n-2)
    return fib(n - 1) + fib(n - 2);
}
