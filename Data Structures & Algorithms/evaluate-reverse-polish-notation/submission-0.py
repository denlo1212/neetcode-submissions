class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("+", "-", "*", "/")
        values = []

        for token in tokens:

            if token not in operators:
                print(token)
                values.append(int(token))
            else:
                b = values.pop()  # Pop the second operand
                a = values.pop()  # Pop the first operand

                if token == "+":
                    values.append(a + b)
                elif token == "-":
                    values.append(a - b)
                elif token == "*":
                    values.append(a * b)
                elif token == "/":
                    values.append(int(a / b))

        return values[0]