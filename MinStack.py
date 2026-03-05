"""
    Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

    Each function should run in O(1)O(1) time.
"""

class MinStack:
    def __init__(self):
        self.minStack = []
        self.array = [] 

    def push(self, val: int) -> None:
        if len(self.array) == 0:
            self.minStack.append(val)
            self.array.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
            self.array.append(val)


    def pop(self) -> None:
        if len(self.array) != 0:
            self.array.pop()
            self.minStack.pop()
        

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        

def test(operations, values, expected):
    obj = None
    results = []
    for op, val, exp in zip(operations, values, expected):
        if op == "MinStack":
            obj = MinStack()
            results.append(None)
        elif op == "push":
            obj.push(val)
            results.append(None)
        elif op == "pop":
            obj.pop()
            results.append(None)
        elif op == "top":
            results.append(obj.top())
        elif op == "getMin":
            results.append(obj.getMin())

    assert results == expected, f"Expected {expected}, got {results}"
    print(f"PASSED: {results}")

operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
values =     [None,       -2,     0,      -3,      None,     None,  None,  None]
expected =   [None,       None,   None,   None,    -3,       None,  0,     -2]

test(operations, values, expected)
