class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right = len(heights) - 1
        waterTrapped = 0
        while left <right:
            hei = min(heights[left],heights[right])
            water = right - left
            area = hei * water

            waterTrapped = max(waterTrapped,area)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return waterTrapped

