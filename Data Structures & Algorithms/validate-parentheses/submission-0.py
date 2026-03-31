class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # key : value
        closeToOpen = {')' : '(', ']' : '[', '}' : '{' }

        # Iterate through every character in the input string
        for c in s:
            # Check if it's a closing parenthesis because every key in the dictionary is a closing parenthesis
            if c in closeToOpen:
                # In python, stack[-1] is the last value added to the stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # If the stack is empty or the parentheses don't match, return false
                else:
                    return False
            # If we get an open parenthesis
            else: 
                stack.append(c)
        
        return True if not stack else False


       
