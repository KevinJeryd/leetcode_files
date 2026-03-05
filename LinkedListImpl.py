from typing import List

class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        
        current = self.head
        for i in range(index):
            current = current.next_node
            if current is None:
                return -1
        
        return current.val

    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        if self.head is None and self.tail is None:
            self.head = newHead
            self.tail = self.head
        else:
            newHead.next_node = self.head
            self.head = newHead

    def insertTail(self, val: int) -> None:
        newTail = Node(val)
        if self.head is None:
            self.head = newTail
            self.tail = newTail
        else:
            self.tail.next_node = newTail
            self.tail = newTail
        
    def remove(self, index: int) -> bool:
        # Nothing to remove if the list is empty
        if self.head is None:
            return False

        if index == 0:
            # If list is only 1 node long
            if self.head.next_node is None:
                self.tail = None
                self.head = None
                return True

            # Otherwise update head
            self.head = self.head.next_node
            return True

        current = self.head
        # Stop one before to be able to set next_node.next_node to "hop over" the removal node
        for _ in range(index-1):
            current = current.next_node
            if current is None:
                return False
        
        # If removal node is out of bounds
        if current.next_node is None:
            return False

        # If the node to remove is tail
        if current.next_node.next_node is None:
            self.tail = current
            current.next_node = None
            return True

        current.next_node = current.next_node.next_node
        return True

    def getValues(self) -> List[int]:
        values = []

        current = self.head
        while current is not None:
            values.append(current.val)
            current = current.next_node
        
        return values
