class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket={"}":"{","]":"[",")":"("}
        for i in s:
            if i in bracket.values():
                stack.append(i)
            elif i in bracket.keys():
                if stack and stack[-1]==bracket[i]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

        