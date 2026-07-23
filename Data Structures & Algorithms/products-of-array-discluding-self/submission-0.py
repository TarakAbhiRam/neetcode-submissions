class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix = [1],[1]
        temp = 1
        for i in nums[:len(nums)-1]:
            temp*=i
            prefix.append(temp)
        print(prefix)

        temp =1
        for i in nums[::-1]:
            temp*=i
            suffix.append(temp)
        suffix.pop()
        suffix.reverse()
        

        print(suffix)
        i=0
        ans=[]
        while i < len(prefix):
            temp = suffix[i]*prefix[i]
            ans.append(temp)
            i+=1
        
        return ans

