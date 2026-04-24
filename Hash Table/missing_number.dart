/*
 * LeetCode: Missing Number
 * Level: Easy 🟢
 *
 * Description:
 * Given an array nums containing n distinct numbers in the range [0, n], 
 * return the only number in the range that is missing from the array.
 *
 * Approach: Mathematical Sum (Gauss Formula)
 * Time Complexity: O(N) - Where N is the length of the input list.
 * Space Complexity: O(1) - Only constant extra space is used.
 */

class Solution {
  int missingNumber(List<int> nums) {
    // n represents the maximum possible number in the range [0, n]
    int n = nums.length;

    // Calculate the expected sum of all numbers from 0 to n using Gauss Formula
    // In Dart, ~/ is used for integer division to ensure the result is an int
    int expectedSum = n * (n + 1) ~/ 2;

    // Calculate the actual sum of the elements present in the list
    int actualSum = 0;
    for (int num in nums) {
      actualSum += num;
    }

    // The difference between the expected sum and actual sum is the missing number
    return expectedSum - actualSum;
  }
}
