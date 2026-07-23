class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers= set(nums)
        longest = 0
        for i in numbers:
            #find starting point
            if i-1 not in numbers:
                length = 0 
                #iterate one by one and increment length
                while i+length in numbers:
                    length += 1
                    longest = max(length,longest)
        return longest
