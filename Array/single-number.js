"""
LeetCode: Single Number
Level: Easy 🟢

Description:
Given a non-empty array of integers 'nums', every element appears twice 
except for one. Find that single one.

Approach: Bitwise XOR Manipulation
- Time Complexity: O(n) - We iterate through the array once.
- Space Complexity: O(1) - No extra data structures used.

Note:
XORing a number with itself cancels it out (a ^ a = 0), 
leaving only the unique number at the end.
"""

var singleNumber = function(nums) {
    let result = 0;

    for (let n of nums) {
        // Apply XOR between the current result and the next number
        result ^= n;
    }

    return result;
};
