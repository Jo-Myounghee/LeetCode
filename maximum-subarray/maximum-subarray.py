class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = -1e9
        _now = 0
        for i in range(len(nums)):
            if _now < 0:
                _now = nums[i]
            else:
                _now += nums[i]
            _max = max(_max, _now)
                
        return _max