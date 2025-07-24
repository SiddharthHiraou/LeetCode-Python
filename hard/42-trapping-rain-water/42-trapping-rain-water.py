                else:
                    total_water += left_max - height[left]
                    left_max = height[left]
                if height[left] >= left_max:
        while left < right:
            if height[left] < height[right]:
        left_max = right_max = 0
        total_water = 0
    def trap(self, height):
        left, right = 0, len(height) - 1
class Solution(object):