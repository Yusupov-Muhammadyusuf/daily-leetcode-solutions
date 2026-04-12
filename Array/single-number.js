/**
 * LeetCode: Single Number
 * Level: Easy 🟢
 
 * * Description:
 * Given a non-empty array of integers 'nums', every element appears twice except for one. 
 * Find that single one.
 
 * * Constraints:
 * You must implement a solution with a linear runtime complexity O(n) 
 * and use only constant extra space O(1).
 
 * * Approach: Bitwise XOR Manipulation
 * - If we XOR a number with itself, it becomes 0 (a ^ a = 0).
 * - If we XOR a number with 0, it stays the same (a ^ 0 = a).
 * - XOR is commutative, so the order doesn't matter. All pairs will cancel out, 
 * leaving only the single number.
 
 * * Time Complexity: O(n) - We iterate through the array once.
 * Space Complexity: O(1) - No extra data structures used.
 */

var singleNumber = function(nums) {
    let result = 0;

    for (let n of nums) {
        // Apply XOR between the current result and the next number
        result ^= n;
    }

    return result;
};
