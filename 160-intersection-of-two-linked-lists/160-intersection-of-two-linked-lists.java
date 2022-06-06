/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode m = headA;
        ListNode n = headB;
        ArrayList ans = new ArrayList();
        while(m!=null){
            ans.add(m);
            m = m.next;
        }
        while(n!=null){
            if (ans.contains(n))
                return n;
                n = n.next;
                }
        return null;
    }
}