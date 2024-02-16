# https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []
        n = len(nums)

        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if current == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif current > 0:
                    k -= 1
                else:
                    j += 1

        return triplets


print(Solution().threeSum([0, 0, 0, 0]))
