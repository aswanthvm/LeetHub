class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        min_len = min(len(s) for s in strs)

        result = ""
        for i in range(min_len):
            char = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != char:
                    return result
            result += char
        return result

        