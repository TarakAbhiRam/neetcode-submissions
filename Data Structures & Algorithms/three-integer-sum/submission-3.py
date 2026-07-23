class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue


            complement = -1 * a
            l,r = i+1,len(nums)-1
            while l < r :
                twosum = nums[l]+nums[r]
                if twosum == complement:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif twosum < complement:
                    l+=1
                else:
                    r-=1
        return res
                    
        
                
