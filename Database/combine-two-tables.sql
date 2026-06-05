"""
LeetCode: Combine Two Tables
Level: Easy 🟢

Description:
Given two tables, Person and Address, write a SQL query to report the 
firstName, lastName, city, and state for each person in the Person table. 
If the address of a personId is not present in the Address table, report null instead.

Approach: Left Join
Time Complexity: O(n + m) - Where n and m are the number of rows in Person and Address tables respectively.
Space Complexity: O(n) - To store the output result.
"""
  
-- Select the required columns from both tables
SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state
-- Start with the Person table to ensure all individuals are included
FROM Person p 
-- Use LEFT JOIN to include people even if they don't have a matching address (returns NULL)
LEFT JOIN Address a ON p.personId = a.personId;
