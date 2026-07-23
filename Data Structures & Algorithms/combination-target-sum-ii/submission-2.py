class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        candidates.sort()

        def dfs(i, cur ,total):
            if total == target:
                ans.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            
            #decision 1
            cur.append(candidates[i])
            dfs(i+1 ,cur,total+candidates[i])
            
            #decision 2
            cur.pop()
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,cur,total)
        dfs(0,cur,0)
        return ans
            
