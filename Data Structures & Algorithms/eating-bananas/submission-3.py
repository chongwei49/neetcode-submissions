class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = result = max(piles)

        while left <= right:
            mid = (right + left) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / mid)
   
            
            if totalTime <= h:
                result = mid
                right = mid - 1 
            else:
                left = mid + 1
        
        return result

            




        