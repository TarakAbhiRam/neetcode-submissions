import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = max(piles)
        
        def hours(rate: int) -> int:
            return sum(math.ceil(pile / rate) for pile in piles)

        l , r = 1 , rate

        while l <= r:
            mid = l + (r-l)//2

            k = hours(mid)
            if k <= h:
                result = mid
                r= mid -1
            elif k > h:
                l= mid+1
        return result
            

