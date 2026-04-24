/**
 * LeetCode: Reverse Linked List
 * Level: Easy 🟢
 * * Description:
 * Given the head of a singly linked list, reverse the list, and return the reversed list.
 * * Example:
 * Input: head = [1,2,3,4,5]
 * Output: [5,4,3,2,1]
 * * Approach: Iterative (Three Pointers)
 * 1. We maintain three pointers: 'prev', 'curr', and 'nextNode'.
 * 2. As we traverse, we flip the 'curr.next' pointer to point backwards to 'prev'.
 * 3. Then we shift 'prev' and 'curr' one step forward.
 * 4. Finally, 'prev' becomes the new head of the reversed list.
 * * Time Complexity: O(n) - We visit each node exactly once.
 * Space Complexity: O(1) - We only use pointers, no extra data structures.
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
 * @return {ListNode}
 */
var reverseList = function(head) {
    // 'prev' will eventually become the new head
    let prev = null;
    // 'curr' starts at the original head
    let curr = head;

    while (curr) {
        // 1. Save the next node before we break the link
        let nextNode = curr.next;
        
        // 2. Reverse the link: current node now points back to the previous node
        curr.next = prev;
        
        // 3. Move 'prev' and 'curr' one step forward
        prev = curr;
        curr = nextNode;
    }

    // After the loop, 'prev' is the last node we processed, which is the new head
    return prev;
};
