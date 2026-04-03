"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we take this type of dict for making appending the world with the 
        # same set of letters: res[(0,0,1...)].append("word")

        res = defaultdict(list)

        for s in strs:
            # make the alphabet list [0, 0, 0...0]
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # Here you have filled alphavet code and you can create the list
            res[tuple(count)].append(s)
        
        return list(res.values())