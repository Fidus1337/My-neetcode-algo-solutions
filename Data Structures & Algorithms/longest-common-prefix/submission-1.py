"""
You are given an array of strings strs. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string "".

Example 1:
Input: strs = ["bat","bag","bank","band"]

Output: "ba"

Example 2:
Input: strs = ["dance","dag","danger","damage"]

Output: "da"
"""
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