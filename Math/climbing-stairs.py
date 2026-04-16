"""
LeetCode: Climbing Stairs
Level: Easy 🟢

Description:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways 
can you climb to the top?

Approach: Dynamic Programming (Iterative / Fibonacci Sequence)
Time Complexity: O(n) - We iterate through the steps once from 3 to n.
Space Complexity: O(1) - We only store the last two calculated values.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 step = 1 way, 2 steps = 2 ways
        if n <= 2:
            return n

        # We use a bottom-up approach (similar to Fibonacci)
        # first represents ways to reach (n-2), second represents (n-1)
        first = 1
        second = 2

        # The number of ways to reach step 'i' is the sum of ways to 
        # reach the previous two steps
        for i in range(3, n + 1):
            now = first + second
            first = second
            second = now

        # 'second' now holds the total ways to reach the n-th step
        return second
