class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(i):
            if i == len(nums):
                answer.append(temp[:])
                return
            for j in range(len(nums)):
                if not visited[j]:
                    temp.append(nums[j])
                    visited[j] = True
                    perm(i+1)
                    temp.pop()
                    visited[j] = False
        
        answer = []
        temp = []
        visited = [False] * len(nums)
        perm(0)
        return answer
        