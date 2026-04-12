class Solution:
    """
    Problem: Two Sum
    Description:
    Given an array of integers 'nums' and an integer 'target', return indices of the 
    two numbers such that they add up to 'target'.
    
    Approach: Brute Force
    - Time Complexity: O(n^2) - because of the nested loops.
    - Space Complexity: O(1) - no extra data structures used.
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        
        # Outer loop to iterate through each element as the first number
        for i in range(n):
            # Inner loop to check all subsequent elements as the second number
            for j in range(i + 1, n):
                # Check if the sum of the two elements equals the target
                if nums[i] + nums[j] == target:
                    # Return the indices of the two numbers
                    return [i, j]

# Example usage:
# nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
