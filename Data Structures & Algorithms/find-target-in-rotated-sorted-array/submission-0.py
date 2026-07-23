class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums)-1

        while l<=r :
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
            
            #mid is in left sorted
            if nums[l]<= nums[mid]:
                if target > nums[mid] or target < nums[l]: #target not in left
                    l = mid+1
                else:
                    r = mid -1
            #mid is in right sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

        


        