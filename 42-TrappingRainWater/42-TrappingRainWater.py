# Last updated: 7/24/2025, 11:26:46 PM
class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1

        return total_water
        