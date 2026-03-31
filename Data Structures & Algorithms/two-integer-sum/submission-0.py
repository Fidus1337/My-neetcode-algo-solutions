class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_hash_table = {}

        for index, i in enumerate(nums):
            diff = target - i

            if diff in diff_hash_table:
                return [diff_hash_table[diff], index]

            diff_hash_table[i] = index
        

