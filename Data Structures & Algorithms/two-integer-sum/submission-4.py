class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        toosom = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in toosom:
                return [toosom[complement],i]
            
            toosom[num]=i
        return []