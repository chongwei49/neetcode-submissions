class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for idx, val in enumerate(numbers):
            hashmap[val] = idx + 1
        
        print(hashmap)
        for key in hashmap:
            tmp = target - key
            if tmp in hashmap:
                if hashmap[tmp] != hashmap[key]:
                    return sorted([hashmap[tmp], hashmap[key]])