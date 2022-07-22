/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode rabbit = head;
        ListNode turtle = head;
        while(rabbit.next!=null && rabbit.next.next!=null){
            turtle = turtle.next;
            rabbit = rabbit.next.next;
        }
        if(rabbit.next!=null){
            turtle = turtle.next;
        }
        return turtle;
    }
}