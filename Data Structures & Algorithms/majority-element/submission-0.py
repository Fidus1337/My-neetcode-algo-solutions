"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [5,5,1,1,1,5,5]

Output: 5
Example 2:

Input: nums = [2,2,2]

Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers_dict = {}
        num_len = len(nums)

        for i in nums:
            numbers_dict[i] = numbers_dict.get(i, 0) + 1

            if numbers_dict[i] > num_len / 2:
                return i