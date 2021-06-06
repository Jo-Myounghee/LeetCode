class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb(s):
            if sum(temp) == target:
                answer.append(temp[:])
            elif sum(temp) < target:
                for i in range(s, len(candidates)):
                    temp.append(candidates[i])
                    comb(i)
                    temp.pop()
            return
        
        answer = []
        temp = []
        comb(0)
        return answer