class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:

            if i == '(':
                stack.append(')')

            elif i == '[':
                stack.append(']')

            elif i == '{':
                stack.append('}')

            else:
                if not stack:
                    return False

                if stack.pop() != i:
                    return False

        return len(stack) == 0