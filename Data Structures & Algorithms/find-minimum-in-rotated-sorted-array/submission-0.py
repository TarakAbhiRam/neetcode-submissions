class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[l] < nums[mid]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] < nums[r]:
                    return nums[l]
                else:
                    return nums[l]
            else:
                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] < nums[r]:
                    r = mid
                else:
                    return nums[mid]

        return nums[l]
