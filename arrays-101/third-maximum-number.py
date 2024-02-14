# https://leetcode.com/problems/third-maximum-number/description/

import math


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first_max = -math.inf
        second_max = -math.inf
        third_max = -math.inf

        for n in nums:
            if n > first_max:
                third_max = second_max
                second_max = first_max
                first_max = n
            if n > second_max and n < first_max:
                third_max = second_max
                second_max = n
            if n > third_max and n < second_max:
                third_max = n

        return third_max if third_max != -math.inf else first_max
