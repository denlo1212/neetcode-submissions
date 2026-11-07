class Solution:
    def isValid(self, string: str) -> bool:
        closedBrackets = {")": "(", "]": "[", "}": "{"}
        stack = []

        for character in string:
            if character not in closedBrackets:
                stack.append(character)

            else:
                if not stack or stack[-1] != closedBrackets[character]:
                    return False
                stack.pop()


        return not stack