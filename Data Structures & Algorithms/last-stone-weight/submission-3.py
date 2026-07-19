class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            print(stones)
            last = heapq.heappop_max(stones)
            second_last = heapq.heappop_max(stones)
            print(last, second_last, abs(last-second_last))
            heapq.heappush_max(stones, abs(last-second_last))

        
        return stones[0]
