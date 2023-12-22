class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        memory = set()

        for n in nums:
            if n in memory:
                return True
            memory.add(n)
        return False


print(Solution().containsDuplicate([1, 2, 2, 3]))
