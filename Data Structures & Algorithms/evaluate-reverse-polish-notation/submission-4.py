class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPS = ["+", "-", "*", "/"]

        stack = []
        for token in tokens:
            if token in OPS:
                right = stack.pop()
                left = stack.pop()

                res = None
                match token:
                    case "+":
                        res = left + right
                    case "-":
                        res = left - right
                    case "*":
                        res = left * right
                    case "/":
                        res = int(left / right)
                    case _:
                        raise AssertionError

                stack.append(res)
            else:
                stack.append(int(token))

        assert len(stack) == 1
        return stack.pop()
