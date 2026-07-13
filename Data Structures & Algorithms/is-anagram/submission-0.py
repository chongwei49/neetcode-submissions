class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping = defaultdict(int)
        for c in s:
            mapping[c] += 1

        for c in t:
            mapping[c] -= 1

        for key in mapping:
            if mapping[key] != 0:
                return False
        
        return True
        