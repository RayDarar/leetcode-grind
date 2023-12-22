# https://leetcode.com/problems/valid-anagram/

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = defaultdict(int)
        for i in range(0, len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1

        for count in counts.values():
            if count != 0:
                return False
        return True
