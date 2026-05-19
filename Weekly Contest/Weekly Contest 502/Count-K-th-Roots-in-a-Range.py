"""
LeetCode: Count K-th Roots in Range [l, r]
Level: Easy 🟢

Description:
Given three integers l, r, and k, count how many integers x exist such that 
their k-th power (x^k) falls within the inclusive range [l, r].

Approach: Linear Scan / Mathematical Simulation
- If k = 1, any number between l and r satisfies the condition, so return r - l + 1.
- Otherwise, start from x = 0 and increment x while x^k is less than or equal to r.
- For each x, if x^k is greater than or equal to l, increment the counter.

Complexity:
- Time Complexity: O(r^(1/k)) — The loop runs at most r^(1/k) times until x^k exceeds r.
- Space Complexity: O(1) — Constant space is used.
"""

class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        # Base case: If k is 1, every integer between l and r is its own 1st root
        if k == 1:
            return r - l + 1

        count = 0
        x = 0

        # Loop as long as the k-th power of x is within the upper bound r
        while x ** k <= r:
            # If the k-th power is also within the lower bound l, it's a valid root
            if x ** k >= l:
                count += 1
            
            # Move to the next integer
            x += 1

        return count
