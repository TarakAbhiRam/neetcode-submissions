class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since array is sorted, let us use two pointer(quick sort)
        left,right = 0,len(numbers)-1
        res=[]
        while left < right:
            complement = target - numbers[left]
            if complement == numbers[right]:
                res.append(left+1)
                res.append(right+1)
                return res
            elif complement < numbers[right]:
                right-=1
            else:
                left+=1
        