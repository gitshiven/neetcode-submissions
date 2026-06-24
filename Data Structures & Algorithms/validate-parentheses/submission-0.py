class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseToOpenBrackets = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in CloseToOpenBrackets:
                if stack and stack[-1]==CloseToOpenBrackets[c]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)

        return True if not stack else False

                    



                