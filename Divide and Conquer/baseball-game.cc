/*
LeetCode: Baseball Game
Level: Easy 🟢

Description:
You are keeping the scores for a baseball game with strange rules. 
You are given a list of strings 'operations', where operations[i] is the ith operation 
you must apply to the record. 
- An integer x: Record a new score of x.
- '+': Record a new score that is the sum of the previous two scores.
- 'D': Record a new score that is the double of the previous score.
- 'C': Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

Approach: Simulation using a Stack/Vector
Time Complexity: O(n) - We iterate through the operations array of size n exactly once.
Space Complexity: O(n) - In the worst case, we store all scores in the vector.
*/

class Solution {
public:
    int calPoints(vector<string>& operations) {
        // Vector to act as a stack to keep track of valid scores
        vector<int> scores;

        // 1. Process each operation one by one
        for (int i = 0; i < operations.size(); i++) {
            if (operations[i] == "+") {
                // Sum of the last two scores
                int total = scores[scores.size() - 1] + scores[scores.size() - 2];
                scores.push_back(total);
            } 
            else if (operations[i] == "D") {
                // Double the last score
                scores.push_back(scores[scores.size() - 1] * 2);
            } 
            else if (operations[i] == "C") {
                // Cancel/remove the last score
                scores.pop_back();
            } 
            else {
                // Convert string to integer and record the new score
                scores.push_back(stoi(operations[i]));
            }
        }

        // 2. Calculate the total sum of all remaining scores
        int sum = 0;
        for (int score : scores) {
            sum += score;
        }

        return sum;
    }
};
