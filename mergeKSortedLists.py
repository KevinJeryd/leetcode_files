from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        l = 0
        # We use len(lists) - 1 instead of len(lists) because l and r are indices,
        # not lengths. The last valid index of any array is always length minus 1.
        r = len(lists) - 1
        
        return self.divide(lists, l, r)
    
    def divide(self, lists, l, r):
        # This happens when we have an odd number of lists. For example with 3 lists,
        # mid will be 1, so right side gets divide(lists, 2, 2) which is fine, but
        # left side gets divide(lists, 0, 1), and inside that call mid is 0, so
        # right gets divide(lists, 1, 1) which is fine. No invalid range there.
        # However in edge cases like an empty lists array, l could exceed r,
        # so we guard against that by returning None, which conquer handles safely.
        if l > r:
            return None
        
        # Base case. l and r pointing to the same index means we have narrowed down
        # to a single linked list in this range. A single linked list is already sorted
        # by definition, so we return it as is.
        if l == r:
            return lists[l]
        
        # We compute mid as l + (r - l) // 2 instead of (l + r) // 2 to avoid
        # integer overflow. In Python this does not matter since integers can be
        # arbitrarily large, but it is a good habit from C++ where int overflow is real.
        # This gives us the middle index of the current range, splitting it into
        # left (l to m) and right (m+1 to r).
        m = l + (r - l) // 2
        
        # Recurse on the left half of the lists array. This will keep splitting until
        # it hits the base case and then merge back up, returning one sorted linked list.
        left = self.divide(lists, l, m)
        
        # Recurse on the right half of the lists array. Same process as above,
        # returning one sorted linked list.
        right = self.divide(lists, m + 1, r)
        
        # At this point left and right are both fully sorted linked lists.
        # We merge them into one sorted linked list and return it upward.
        return self.conquer(left, right)
    
    def conquer(self, list1, list2):
        # We create a dummy node with a throwaway value of -1 as a fixed starting point.
        # This lets us always do curr.next = ... without special casing the first node,
        # since we always have a curr to attach to.
        dummy = ListNode(-1)
        curr = dummy
        
        # We compare the current head of each list and pick the smaller one,
        # attach it to curr, and advance both curr and the list we picked from.
        # We use <= instead of < so that when values are equal we pick from list1 first,
        # preserving the original order of equal elements, making the sort stable.
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # When the while loop exits, one list is fully consumed and the other may still
        # have remaining nodes. Since both lists are already sorted, we can safely attach
        # the remainder directly without comparing further.
        # If list1 is not None it has remaining nodes, otherwise list2 does (or both are
        # None in which case we attach None which is harmless).
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        # dummy.next is the real head of the merged list, since dummy itself was just
        # a placeholder we used to avoid special casing the first node.
        return dummy.next
