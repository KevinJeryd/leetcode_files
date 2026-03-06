class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        newHead = Solution.reverseList(self, head.next) # Traverse to the end node, the new head. Save the new head

        # Rearrange the pointers between the nodes
        head.next.next = head       # Point the next nodes next to the current node (reversing the chain)
        head.next = None            # Sever the forward link that the current node still has so it won't be a loop

        # Return the new head, it's what the user wants back, don't alter it.
        return newHead
