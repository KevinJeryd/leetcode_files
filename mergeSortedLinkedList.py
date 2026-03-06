from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Initial solution, my intuition, "brute force"
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            newHead = list1
            secondHead = list2
        else:
            newHead = list2
            secondHead = list1

        dummy = newHead
        head = dummy
        newHead = newHead.next

        while newHead and secondHead:
            if newHead.val < secondHead.val:
                dummy.next = newHead
                dummy = dummy.next
                newHead = newHead.next
            else:
                dummy.next = secondHead
                dummy = dummy.next
                secondHead = secondHead.next

        if newHead is None:
            dummy.next = secondHead
        if secondHead is None:
            dummy.next = newHead

        return head
    
    # Second try, "optimal solution"
    def mergeTwoListsOptimal(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = curr = ListNode(-1)

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
        
        return dummyHead.next

            


def makeList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def toList(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

def test(values1, values2, expected):
    list1 = makeList(values1)
    list2 = makeList(values2)
    result = Solution().mergeTwoLists(list1, list2)
    answer = toList(result)
    assert answer == expected, f"Expected {expected}, got {answer}"
    print(f"PASSED: {answer}")

test([1,2,4], [1,3,5], [1,1,2,3,4,5])
test([], [1,2,3], [1,2,3])
test([1,2,3], [], [1,2,3])
test([], [], [])
test([1], [2], [1,2])

"""
Pattern: Two Pointers

Why: You have two sequences and need to process them together in order. 
     One pointer into each list lets you always compare the current candidates and pick the smaller one, without ever needing to backtrack.

How: Determine the head upfront by comparing the first elements. 
     Then use a pointer to track where you're currently appending. 
     At each step compare the two current nodes, attach the smaller one, and advance that list's pointer. 
     When one list runs out, attach the remainder of the other directly since it's already sorted.
"""
