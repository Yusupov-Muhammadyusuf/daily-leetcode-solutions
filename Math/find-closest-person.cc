/*
LeetCode: Find Closest Person
Level: Easy 🟢

Description:
Given three integers `x`, `y`, and `z`, determine which of the two integers 
(`x` or `y`) is closer to `z`. Return 1 if `x` is closer, 2 if `y` is closer, 
and 0 if they are equidistant (equally close).

Approach: Absolute Difference Comparison
Time Complexity: O(1) - Constant time as it only involves basic arithmetic.
Space Complexity: O(1) - No extra space used.
*/

class Solution {
public:
    int findClosest(int x, int y, int z) {
        // 1. Calculate the absolute distance from x and y to z
        int d1 = abs(x - z);
        int d2 = abs(y - z);

        // 2. Compare distances and return the appropriate result
        if (d1 < d2) {
            return 1; // x is closer
        } else if (d2 < d1) {
            return 2; // y is closer
        } else {
            return 0; // Both are equidistant
        }
    }
};
