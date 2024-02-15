# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_streak = 0
        lookup_set = set(nums)

        for n in lookup_set:
            if n - 1 in lookup_set:
                continue
            next_n = n
            streak = 1

            while next_n + 1 in lookup_set:
                next_n += 1
                streak += 1

            max_streak = max(max_streak, streak)

        return max_streak
