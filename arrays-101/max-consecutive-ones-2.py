# https://leetcode.com/problems/max-consecutive-ones-ii/


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        count = 0
        post_count = 0

        for i in range(0, len(nums)):
            n = nums[i]

            if n == 1:
                count += 1
                post_count += 1
            elif n == 0:
                count = post_count + 1
                post_count = 0

            if count > max_count:
                max_count = count

        return max_count
