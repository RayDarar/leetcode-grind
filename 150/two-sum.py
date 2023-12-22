class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        memory: dict[int, int] = dict()

        for i in range(len(nums)):
            df = target - nums[i]
            if df in memory:
                return [i, memory[df]]
            memory[nums[i]] = i
