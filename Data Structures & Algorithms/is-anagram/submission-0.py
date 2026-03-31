"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false"""

class Solution:
    def count_letters(self, word)->dict:
        chars_count = {}

        for char in word:
            chars_count[char] = chars_count.get(char, 0) + 1
        
        return chars_count

    def isAnagram(self, s: str, t: str) -> bool:
        return self.count_letters(s) == self.count_letters(t)
        