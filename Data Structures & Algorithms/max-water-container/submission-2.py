class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            left = i
            right = i
            while right < len(heights):
                if left == right:
                    right += 1
                    continue
                
                breath = right - left
                area = breath * min(heights[left], heights[right])
                if area > max_area:
                    max_area = area
                right += 1

        return max_area
                
            
        