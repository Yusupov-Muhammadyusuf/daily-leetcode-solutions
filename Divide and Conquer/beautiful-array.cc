/*
LeetCode: Beautiful Array
Level: Medium 🟡

Description:
Given an integer n, return any beautiful array of length n.
An array nums of length n is beautiful if:
1. nums is a permutation of the integers from 1 to n.
2. For every i < j with i + 1 < j, there is no k with i < k < j 
   such that 2 * nums[k] == nums[i] + nums[j].

Approach: Divide and Conquer / Linearity Transformation
Time Complexity: O(n log n) - In each step, we process the elements to form odds and evens.
Space Complexity: O(n) - Used to store the intermediate results and the final beautiful array.
*/

class Solution {
public:
    vector<int> beautifulArray(int n) {
        // 1. Base case: a single element [1] is always a beautiful array
        vector<int> result = {1};

        // 2. Expand the array using divide and conquer logic until its size reaches n
        while (result.size() < n) {
            vector<int> odds;
            vector<int> evens;

            // Generate odd elements using the linear map: 2 * x - 1
            for (int x : result) {
                if (2 * x - 1 <= n) {
                    odds.push_back(2 * x - 1);
                }
            }

            // Generate even elements using the linear map: 2 * x
            for (int x : result) {
                if (2 * x <= n) {
                    evens.push_back(2 * x);
                }
            }

            // Combine odds and evens. 
            // A beautiful array of odds followed by a beautiful array of evens is also beautiful.
            result = odds;
            result.insert(result.end(), evens.begin(), evens.end());
        }   

        // 3. Return the fully constructed beautiful array
        return result;
    }
};
