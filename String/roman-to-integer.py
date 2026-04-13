"""
LeetCode: Roman to Integer
Level: Easy 🟢

Description:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer. The key rule is that if a 
smaller value precedes a larger value, it is subtracted; otherwise, it is added.

Approach: Hash Map & Linear Scan
Time Complexity: O(n) - We iterate through the string 's' once.
Space Complexity: O(1) - The map size is constant (7 symbols).
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        # Define the mapping of Roman symbols to their integer values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            # If the current value is less than the next value, we subtract it
            # Example: IV -> -1 + 5 = 4
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, we add the value to the total
                total += roman_map[s[i]]

        return total
