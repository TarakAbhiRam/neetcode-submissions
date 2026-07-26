class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist =  [0] * len(points)

        i = 0
        for pt in points:

            dist[i] = pt[0]**2 + pt[1]**2
            i+=1
        points = [x for _, x in sorted(zip(dist,points))]
        return points[:k]
