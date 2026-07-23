class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        ans = set()
        nums.sort()
        def dfs(i,subset):
            if i>= len(nums):
                ans.add(tuple(subset))
                return
            
            #decision 1
            subset.append(nums[i])
            dfs(i+1,subset)

            #decision 2
            subset.pop()
            while i+1< len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1,subset)

        dfs(0, subset)
        return [list(s) for s in ans]
