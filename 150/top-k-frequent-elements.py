# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for val, count in counts.items():
            buckets[count].append(val)

        result = []

        for bucket in buckets[::-1]:
            for n in bucket:
                result.append(n)

            if len(result) == k:
                return result

        return result
