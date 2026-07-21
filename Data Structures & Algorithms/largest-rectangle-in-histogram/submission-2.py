class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(index, height)
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
                # print("index:",index,"height:",height,"maxArea",maxArea,"start",start)
            stack.append((start, h))
            # print(stack)
            # print("-")
            
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
