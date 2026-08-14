class Solution:
    def checkValidString(self, s: str) -> bool:
        left , star = [] ,[]
        for i,v in enumerate(s):
            if v == "(":
                left.append(i)
            elif v == "*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while left and star:
            if left[-1] < star[-1]:
                left.pop()
                star.pop()
            else:
                return False
        return not left