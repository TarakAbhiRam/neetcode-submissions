class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        #using only normal heap 
        for i in nums:
            hashmap[i]+=1
        ans=[]
        for i in range(k):
            Maxkey = max(hashmap, key = hashmap.get)
            hashmap.pop(Maxkey)
            ans.append(Maxkey)
        return ans