class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        f=len(s)-1
        while(i<f):
            if not s[i].isalnum():
                i=i+1
            elif not s[f].isalnum():
                f=f-1
            else:
                if s[i].lower()!= s[f].lower():
                    return False
                i=i+1
                f=f-1   
        return True
        