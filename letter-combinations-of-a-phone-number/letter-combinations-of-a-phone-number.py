class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(idx, word):
            if len(word) == len(digits):
                answer.append(word)
                return
            
            for i in range(idx, len(digits)):
                for j in phone[digits[i]]:
                    dfs(i+1, word+j)
        
        if not digits:
            return []
        
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        answer = []
        dfs(0, '')
        
        return answer