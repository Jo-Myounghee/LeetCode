class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def comb(s, i):
            if i == k:
                answer.append(temp[:])
                return
            for j in range(s, n+1):
                temp.append(j)
                comb(j+1, i+1)
                temp.pop()
        
        
        answer = []
        temp = []
        comb(1, 0)
        return answer