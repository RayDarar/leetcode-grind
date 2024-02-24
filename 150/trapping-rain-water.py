# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, heights: list[int]) -> int:
        water = 0
        l, r = 0, len(heights) - 1
        l_max, r_max = 0, 0

        while l < r:
            if heights[l] < heights[r]:
                l_max = max(l_max, heights[l])
                water += l_max - heights[l]
                l += 1
            else:
                r_max = max(r_max, heights[r])
                water += r_max - heights[r]
                r -= 1

        return water
