class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        subset = []

        def backtrack(i):
            if i>= len(nums):
                ans.append(subset.copy())
                return 
            subset.append(nums[i])# if we add a number
            backtrack(i+1)
            subset.pop() #if we dont add
            backtrack(i+1)

        backtrack(0)
        return ans

        