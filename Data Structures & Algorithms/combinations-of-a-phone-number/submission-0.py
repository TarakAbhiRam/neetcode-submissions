class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        combs = []

        def dfs(i):
            if i>= len(digits):
                res.append(''.join(combs))
                return
            for char in num_map[digits[i]]:
                combs.append(char)
                dfs(i+1)
                combs.pop()
        dfs(0)
        return res
