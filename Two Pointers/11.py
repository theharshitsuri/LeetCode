# 11. CONTAINER WITH MOST WATER

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r-l) * min(height[r],height[l])
            if area > ans:
                ans = area
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return ans

        