"""
LeetCode: Cricket Score Validator
Level: Easy 🟢

Description:
Given a list of strings events representing individual ball outcomes 
in a cricket innings. Valid scoring events include runs ("0", "1", "2", 
"3", "4", "6"), wickets ("W"), wide balls ("WD"), and no-balls ("NB"). 

Calculate the total score and the total number of wickets lost. 
The innings automatically ends if the fielding team takes 10 wickets. 
Return the result as a list containing [total_score, wickets_lost].

Approach: Using a Hash Set & Linear Simulation
Time Complexity: O(n) - We traverse the array once.
Space Complexity: O(1) - Constant extra space used.
"""
class Solution:
    def scoreValidator(self, events: List[str]) -> List[int]:
        score = 0
        counter = 0
        # Valid runs that can be scored off a legal delivery
        digits = {"0", "1", "2", "3", "4", "6"}

        for event in events:
            # If runs are scored, add them to the total score
            if event in digits:
                score += int(event)
             
            # If it's a wicket, increase the wicket counter
            if event == "W":
                counter += 1
                # The innings ends if 10 wickets are down
                if counter == 10:
                    break 

            # Extras (Wide / No-Ball) award 1 penalty run to the batting team
            if event == "WD" or event == "NB":
                score += 1

        return [score, counter]
