class Solution:
    def maxDepth(self, s: str) -> int:
        depth = maxdepth = 0
        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            maxdepth = max(maxdepth, depth)
        return maxdepth