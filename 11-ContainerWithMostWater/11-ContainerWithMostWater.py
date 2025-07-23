# Last updated: 7/23/2025, 2:29:11 PM
class Solution(object):
    def maxArea(self, height):
        final_area=0
        l,r=0,len(height)-1
        while(l<r):
            area=min(height[l],height[r])*(r-l)
            final_area=max(final_area,area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return final_area

        