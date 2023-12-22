# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        memory = set()

        for n in nums:
            if n in memory:
                return True
            memory.add(n)
        return False
