class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest =0
        for i in numbers:
            if i-1 not in numbers:  #starting point
                length =0 
                while i+length in numbers:
                    length+=1
                    longest = max(length,longest)
        return longest 
