class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # Input: strs = ["bat","bag","bank","band"] - Output: "ba"
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
            
        return res