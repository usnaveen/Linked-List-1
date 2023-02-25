# Author: Naveen US
# Title: Linked List Cycle II

# Time complexity: O(n)
# Space complexity: O(1)
# Did the code run on leetcode: Yes

class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast is not None:
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            slow = slow.next
            if slow == fast:
                break
        if fast is None:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
