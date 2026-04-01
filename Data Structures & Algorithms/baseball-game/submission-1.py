class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            match op:
                case '+':
                    stack.append(stack[-1] + stack[-2])
                case 'D':
                    stack.append(2 * stack[-1])
                case 'C':
                    stack.pop()
                case _: # Default case
                    stack.append(int(op))
        
        return sum(stack)
