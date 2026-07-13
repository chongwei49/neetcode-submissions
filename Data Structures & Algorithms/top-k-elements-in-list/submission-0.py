class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        
        result = []
        for _ in range(k):
            max_val = 0
            max_key = 0
            for key in hashmap:
                if hashmap[key] > max_val:
                    max_val = hashmap[key]
                    max_key = key
            result.append(max_key)
            del hashmap[max_key]


        return result