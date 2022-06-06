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
        int headAlength=0;
        int headBlength=0;
          ListNode ans=null;
        ListNode a=headA;
        ListNode b= headB;
        while(a.next!=null)
        {
            a=a.next;
            headAlength++;
        }
        
           while(b.next!=null)
        {
            b=b.next;
            headBlength++;
        }
        
        while (headAlength >headBlength)
        {
            headA=headA.next;
            headAlength--;
        }
         while (headBlength >headAlength)
        {
            headB=headB.next;
            headBlength--;
        }
        
        while(headA!=headB)
        {
            headA=headA.next;
            headB=headB.next;
        }
        return headB;
    }
}