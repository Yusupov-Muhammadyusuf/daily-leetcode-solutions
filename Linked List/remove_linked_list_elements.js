/**
 * LeetCode: Remove Linked List Elements
 * Level: Easy 🟢
 * * Description:
 * Given the head of a linked list and an integer val, remove all the nodes 
 * of the linked list that has Node.val == val, and return the new head.
 * * Example: 
 * Input: head = [1,2,6,3,4,5,6], val = 6
 * Output: [1,2,3,4,5]
 * * Approach: Dummy Node (Sentinel Node)
 * 1. We use a 'dummy' node that points to the head to handle cases where 
 * the head node itself needs to be removed.
 * 2. We traverse the list using a 'current' pointer.
 * 3. If 'current.next.val' matches the target value, we skip that node 
 * by changing the 'next' pointer: current.next = current.next.next.
 * 4. Otherwise, we simply move the 'current' pointer forward.
 * * Time Complexity: O(n) - Single pass through the list.
 * Space Complexity: O(1) - Constant extra space used.
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 * this.val = (val===undefined ? 0 : val)
 * this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    // Create a dummy node to act as a precursor to the head
    let dummy = new ListNode(0);
    dummy.next = head;
    
    // 'current' starts at the dummy node
    let current = dummy;

    while (current.next) {
        if (current.next.val === val) {
            // If the next node's value matches, bypass it
            current.next = current.next.next;
        } else {
            // Otherwise, just move the pointer forward
            current = current.next;
        }
    }

    // Return the actual head (which is dummy.next)
    return dummy.next;
};
