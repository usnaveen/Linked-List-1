# Author: Naveen US
# Title: Reverse Linked List

# Time complexity: O(n)
# Space complexity: O(1)
# Did the code run on leetcode: Yes

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        fast = head.next
        curr = head
        while(fast!=None):
            curr.next = prev
            prev = curr 
            curr = fast
            fast = fast.next   
        curr.next = prev  
        return curr 
