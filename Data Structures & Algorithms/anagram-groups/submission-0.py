from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for words in strs:
            Sortwords = ''.join(sorted(words))
            groups[Sortwords].append(words)

        return list(groups.values())
