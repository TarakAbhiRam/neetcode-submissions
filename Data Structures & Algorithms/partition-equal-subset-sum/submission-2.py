class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp = {0}
        for num in nums:
            dp |= {t + num for t in dp}
            if target in dp:
                return True
        return False
