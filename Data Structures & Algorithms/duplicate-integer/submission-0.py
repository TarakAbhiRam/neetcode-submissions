class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for i in nums:
            if i not in ans:
                ans.add(i)
            else:
                return True
        return False