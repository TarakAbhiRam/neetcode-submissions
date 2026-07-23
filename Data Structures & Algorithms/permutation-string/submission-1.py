class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = defaultdict(int)
        def dictify(s):
            d= defaultdict(int)
            for i in s:
                d[i]+=1
            return d

                
        for i in s1:
            window[i]+=1
        size =  len(s1)
        left = 0 
        for i in range(len(s2)-size+1):
            if dictify(s2[i:i+size]) != window:
                i+=1
                continue
            else:
                return True
        return False

            
                