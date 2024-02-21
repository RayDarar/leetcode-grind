# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = {
            "{": "}",
            "[": "]",
            "(": ")",
        }

        pairs = []

        for c in s:
            if c in pair_map:
                pairs.append(c)
            elif pairs and c == pair_map[pairs[-1]]:
                pairs.pop()
            else:
                return False

        return True if not pairs else False
