# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nums = set(nums)
        result = []

        for i in range(1, n + 1):
            if i not in nums:
                result.append(i)

        return result
