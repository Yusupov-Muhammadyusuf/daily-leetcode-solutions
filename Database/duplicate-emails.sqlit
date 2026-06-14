/*
LeetCode: Duplicate Emails
Level: Easy 🟢

Description:
Given a table named 'person', write a SQL query to find all duplicate emails 
in the table. A duplicate email is one that appears more than once.

Approach: GROUP BY & HAVING Clause
Time Complexity: O(N) - Where N is the number of rows in the person table.
Space Complexity: O(N) - To group and store the unique emails in memory.
*/

SELECT email
FROM person
GROUP BY email
HAVING COUNT(email) > 1;
