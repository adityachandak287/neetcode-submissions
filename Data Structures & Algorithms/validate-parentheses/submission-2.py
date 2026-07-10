class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching_pairs = {")": "(", "}": "{", "]": "["}

        for c in s:
            match c:
                case "(" | "{" | "[":
                    stack.append(c)
                case ")" | "}" | "]":
                    if len(stack) == 0:
                        return False
                    if stack[-1] != matching_pairs[c]:
                        return False
                    stack.pop()

        if len(stack) > 0:
            return False

        return True
