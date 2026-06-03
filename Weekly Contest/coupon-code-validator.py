"""
LeetCode: Validate Coupons
Level: Easy/Medium 🟡

Description:
Given lists of coupon codes, their corresponding business lines, and their active status,
filter out only the valid and active coupons based on specific criteria.

A coupon is considered valid if:
1. It is active (isActive[i] == True).
2. The business line is one of "electronics", "grocery", "pharmacy", or "restaurant".
3. The coupon code is non-empty and contains only alphanumeric characters or underscores (_).

The final result should be sorted alphabetically within each business line, and the groups 
must be concatenated in the following specific order: 
Electronics -> Grocery -> Pharmacy -> Restaurant.

Approach: Filtering & Grouped Sorting
Time Complexity: O(N log N) - Filtering takes O(N) time, and sorting the groups takes 
                 O(N log N) in the worst case where all coupons belong to a single category.
Space Complexity: O(N) - Additional lists are used to store and group the valid coupons.
"""

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # Separate lists to gather coupons for each business line
        electronics = []
        grocery = []
        pharmacy = []
        restaurant = []

        # Iterate through all lists simultaneously using indices
        for i in range(len(code)):
            # Condition 1: Coupon must be active and belong to a valid business line
            if isActive[i] and businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"]:
                c = code[i]
                
                # Condition 2: Code must be non-empty and contain only alphanumeric chars or '_'
                if c and all(char.isalnum() or char == "_" for char in c):
                    # Append to the corresponding category
                    if businessLine[i] == "electronics":
                        electronics.append(c)
                    elif businessLine[i] == "grocery":
                        grocery.append(c)
                    elif businessLine[i] == "pharmacy":
                        pharmacy.append(c)
                    elif businessLine[i] == "restaurant":
                        restaurant.append(c)
        
        # Sort each group alphabetically
        electronics.sort()
        grocery.sort()
        pharmacy.sort()
        restaurant.sort()

        # Concatenate and return the results in the required category order
        return electronics + grocery + pharmacy + restaurant
