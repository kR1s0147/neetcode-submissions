class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return [] 

        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        result = []     
        current_combination = []

        def backtrack(index):    
            if index == len(digits):
                result.append("".join(current_combination))
                return

            digit = digits[index]
          
            if digit not in mapping:
                return

            letters = mapping[digit]

            for letter in letters: 
                current_combination.append(letter)  
                backtrack(index + 1)
                current_combination.pop()
              
        backtrack(0)
        return result