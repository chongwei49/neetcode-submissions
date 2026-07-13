class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # [[temp, day]]

        for day, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, d = stack.pop()
                result[d] = day - d
                
            stack.append([temp, day])
        
        return result
        