class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        window = collections.deque()
        for i in range(len(nums)):
            if window and i-window[0] == k:
                window.popleft()
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
            if i+1 >= k:
                answer.append(nums[window[0]])
        return answer