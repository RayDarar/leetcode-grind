# https://leetcode.com/problems/squares-of-a-sorted-array/description/


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1

        result = []

        while left < right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] * nums[left])
                left += 1
            else:
                result.append(nums[right] * nums[right])
                right -= 1
        result.append(nums[left] * nums[left])

        return result[::-1]
