class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        answer = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            if stack:
                while stack and stack[-1][1] < temp:
                    pre_idx, pre_temp = stack.pop()
                    answer[pre_idx] = idx-pre_idx
            stack.append((idx, temp))
        return answer