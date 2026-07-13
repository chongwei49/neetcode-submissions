class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(list(set(nums)))
        return (len(list(set(nums))) != len(nums))