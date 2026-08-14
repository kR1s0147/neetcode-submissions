class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack =[]

        def backtrack(openb,closeb):
            if openb == n and closeb == n :
                res.append("".join(stack))
                return
            if openb <n:
                stack.append("(")
                backtrack(openb+1,closeb)
                stack.pop()
            if closeb < openb:
                stack.append(")")
                backtrack(openb,closeb+1)
                stack.pop()
            
        backtrack(0,0)
        return res