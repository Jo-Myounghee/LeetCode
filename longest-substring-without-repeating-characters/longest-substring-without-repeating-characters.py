class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len = start = 0
        for idx, word in enumerate(s):
            if word in used and start <= used[word]:
                start = used[word] + 1
            else:
                max_len = max(max_len, idx - start + 1)
            used[word] = idx
        
        return max_len