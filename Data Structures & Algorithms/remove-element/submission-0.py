class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
        
        new_l = [i for i in nums if i is not None]

        for i in range(len(new_l)):
            nums[i] = new_l[i]
            
        return len(new_l)