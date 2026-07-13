class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val_i in enumerate(nums):
            for j, val_j in enumerate(nums):
                if i != j:
                    if val_i + val_j == target:
                        return [i, j]

