class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = Counter(s1)

        size =  len(s1)
        left = 0 
        for i in range(len(s2)-size+1):
            if Counter(s2[i:i+size]) != window:
                i+=1
                continue
            else:
                return True
        return False

            
                