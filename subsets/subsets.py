class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subset(i, k):
            if i == k:
                answer.append(temp[:])
                return
            for j in range(i, len(nums)):
                temp.append(nums[j])
                subset(j+1, k)
                temp.pop()
        
        answer = []
        temp = []
        for i in range(len(nums)+1):
            subset(0, i)
        return answer