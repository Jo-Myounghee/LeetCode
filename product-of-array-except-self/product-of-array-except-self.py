class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        temp = 1

        for i in range(len(nums)):
            answer.append(temp)
            temp *= nums[i]
        temp = 1

        for i in range(len(nums)-1, -1, -1):
            answer[i] *= temp
            temp *= nums[i]
        return answer