class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in anagrams:
                anagrams[sort_s].append(s)
            else:
                anagrams[sort_s] = [s]
        
        return anagrams.values()
            