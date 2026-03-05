"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { 
                ")" : "(",
                "]" : "[",
                "}" : "{"
                }

        for char in s:
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

def Test(input, expected):
    answer = Solution().isValid(input)
    assert answer == expected, f"answer = {answer}, expected = {expected}"
    print("PASSED!")

s = "()"
Test(s, True)

s = "()[]{}"
Test(s, True)

s = "(]"
Test(s, False)

s = "([])"
Test(s, True)

s = "([)]"
Test(s, False)

"""
Pattern: Stack

Why: Use a stack when the most recent thing you saw is the most important thing to deal with next.
     In this case, the last opened bracket is always the one that needs to be closed first.

How: Iterate through each character. If it's an opening bracket, push it onto the stack.
     If it's a closing bracket, check if the top of the stack is its matching opener.
     If it matches, pop the stack. If it doesn't match, or the stack is empty, the string is invalid.
     After the full iteration, the string is only valid if the stack is empty,
     meaning every opener was correctly closed.
"""
