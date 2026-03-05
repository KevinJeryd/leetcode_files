# Problem Description:
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr:
            next = curr.next # Save so we don't lose our next after we overwrite the current.next one step back
            curr.next = prev # Set the currents next to the one before for the "reversing effect"
            prev = curr # Move previous forward so that next loop we can point to this as the new prev
            curr = next # And move the current forward to our saved next
        
        return prev # At the end curr will be null because we set it to next at the end of the loop which will be out of bound, the new head is prev




#####################################################
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

def test(values, expected):
    head = makeList(values)
    result = Solution().reverseList(head)
    answer = toList(result)
    assert answer == expected, f"Expected {expected}, got {answer}"
    print(f"PASSED: {answer}")

test([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
test([1, 2], [2, 1])
test([1], [1])
test([], [])
#####################################################
