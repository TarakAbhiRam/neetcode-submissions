class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        def permute(use :set,cur:List[int]):
            if not use:
                ans.append(cur.copy())
                return
            for num in list(use):
                cur.append(num)
                use.remove(num)
                permute(use,cur)
                cur.pop()
                use.add(num)

        permute(set(nums), cur)
        return ans
            
