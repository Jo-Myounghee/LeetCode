class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i
        
        for i, num in enumerate(nums):
            if target - num in nums_dict and i != nums_dict[target-num]:
                return nums.index(num), nums_dict[target-num]