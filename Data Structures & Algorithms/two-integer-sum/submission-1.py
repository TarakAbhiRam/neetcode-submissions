class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        index=0

        for num in nums:
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement],index]
            hashmap[num] = index
            index+=1
        return []