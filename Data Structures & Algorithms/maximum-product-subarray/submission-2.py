class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]

        # forward
        maxi = 1
        for i in range(n):
            maxi *= nums[i]
            ans = max(ans, maxi)
            if maxi == 0:
                maxi = 1

        # backward
        mini = 1
        for i in range(n - 1, -1, -1):
            mini *= nums[i]
            ans = max(ans, mini)
            if mini == 0:
                mini = 1

        return ans
