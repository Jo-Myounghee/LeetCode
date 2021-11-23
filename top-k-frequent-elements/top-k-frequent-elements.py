class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = collections.Counter(nums)
        heap = []
        for key in cnts:
            heapq.heappush(heap, (-cnts[key], key))
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer