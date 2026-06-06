"""
LeetCode: Left and Right Sum Differences
Level: Easy 🟢

Description:
Given a 0-indexed integer array nums, find a 0-indexed integer array answer of the same length where:
answer[i] = |leftSum[i] - rightSum[i]|

Approach: Prefix and Suffix Sum Arrays
Time Complexity: O(n) - The array is iterated 3 separate times, which takes linear time.
Space Complexity: O(n) - Additional arrays are used to store left and right sums.
"""

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initialize arrays for left sums, right sums, and the final answer
        leftSum = [0] * n
        rightSum = [0] * n
        answer = [0] * n

        # 1. Calculate the sum of elements to the left of each index
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]

        # 2. Calculate the sum of elements to the right of each index
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]
        
        # 3. Calculate the absolute difference between leftSum and rightSum
        for i in range(n):
            answer[i] = abs(leftSum[i] - rightSum[i])
        
        # Return the final calculated answer array
        return answer
