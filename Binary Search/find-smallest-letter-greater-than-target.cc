/*
LeetCode: Find Smallest Letter Greater Than Target
Level: Easy 🟢

Description:
Given a characters array `letters` that is sorted in non-decreasing order, 
and a character `target`, return the smallest character in the array that is 
larger than `target`. If such a character does not exist, return the first 
character in `letters`.

Approach: Binary Search
Time Complexity: O(log n) - The search space is halved in each step.
Space Complexity: O(1) - No extra space is used except for pointers.
*/

char nextGreatestLetter(char* letters, int lettersSize, char target) {
    int low = 0;
    int high = lettersSize - 1;

    // 1. Perform Binary Search to find the smallest element greater than target
    while(low <= high) {
        int mid = low + (high - low) / 2;
        
        // If the middle character is less than or equal to target, search the right half
        if (letters[mid] <= target) {
            low = mid + 1;
        } 
        // Otherwise, search the left half
        else {
            high = mid - 1;
        }
    }

    // 2. Return the correct character. If 'low' goes out of bounds, 
    // the modulo operation wraps it around to the first element (index 0).
    return letters[low % lettersSize];
}
