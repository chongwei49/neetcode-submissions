class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:    
        result = [] 
        def bt(start, path):
            nonlocal result
            result.append(path)
            for i in range(start, len(nums)):
                bt(i+1, path+[nums[i]])
        
        bt(0, [])

        return result