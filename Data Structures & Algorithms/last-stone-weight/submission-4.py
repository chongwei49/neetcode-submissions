class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            last = heapq.heappop_max(stones)
            second_last = heapq.heappop_max(stones)
            heapq.heappush_max(stones, abs(last-second_last))

        
        return stones[0]
