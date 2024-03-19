# 20. Valid parenthesis
class Solution(object):
    def isValid(self, s):
        stack = []
        if len(s) == 1 or len(s) % 2 != 0:
            return False

        if s[0] in ')}]':
            return False

        for char in s:
            if char in '{([':
                stack.append(char)
            elif stack:
                if char == '}' and stack[-1] != '{' or \
                        char == ')' and stack[-1] != '(' or \
                        char == ']' and stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            else:
                if char == '}' and not stack or \
                        char == ')' and not stack or \
                        char == ']' and not stack:
                    return False

        if stack:
            return False
        else:
            return True


solution = Solution()
print(solution.isValid('())'))

# O(n)
