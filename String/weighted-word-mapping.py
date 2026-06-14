"""
LeetCode: Map Word Weights
Level: Easy 🟢

Description:
Given a list of strings 'words' and an integer array 'weights' representing the 
weight of each lowercase English letter. For each word, calculate the total weight 
of its characters. Find the remainder (modulo) of the total weight when divided by 26, 
and map it in reverse order (25 - modulo) to a new character. Finally, combine 
the mapped characters of all words and return them as a single string.

Approach: Character ASCII Manipulation & Linear Scan
Time Complexity: O(N * M) - Where N is the number of words and M is the average length of a word.
Space Complexity: O(N) - To store the resulting characters and join them into the final string.
"""

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []

        for word in words:
            total_weights = 0
            
            # Iterate through each character to calculate the total weight of the word
            for ltr in word:
                # Convert the character to a 0-indexed integer (a -> 0, b -> 1, ..., z -> 25)
                idx = ord(ltr) - ord("a")
                total_weights += weights[idx]

            # Get the modulo of the total weight by 26
            modulo = total_weights % 26
            
            # Map the modulo value in reverse order (e.g., 0 becomes 25, which is 'z')
            ans_idx = 25 - modulo

            # Convert the final index back to its corresponding character
            mapped_char = chr(ans_idx + ord("a"))
            result.append(mapped_char)
        
        # Join all the mapped characters into a single string
        return "".join(result)
