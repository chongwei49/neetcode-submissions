class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        left_product = 1
        right_product = 1
        
        for i in range(n):
            res[i] *= left_product
            left_product *= nums[i]
            
            res[n - 1 - i] *= right_product
            right_product *= nums[n - 1 - i]
            
        return res

        