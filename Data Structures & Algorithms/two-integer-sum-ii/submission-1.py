class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since array is sorted, let us use two pointer(quick sort)
        left,right = 0,len(numbers)-1

        while left < right:
            complement = target - numbers[left]
            if complement == numbers[right]:
                return[left+1,right+1]
            elif complement < numbers[right]:
                right-=1
            else:
                left+=1
        