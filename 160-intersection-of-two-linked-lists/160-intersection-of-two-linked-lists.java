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
        Set<ListNode> ans = new HashSet<ListNode>();
        while(m!=null){
            ans.add(m);
            m = m.next;
        }
        m = headB;
        while(m!=null){
            if (ans.contains(m))
                return m;
                m = m.next;
            }
        return null;
    }
}