class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for words in strs:
            count = [0] * 26
            for char in words:
                count[ord(char)- ord('a')] += 1
            groups[tuple(count)].append(words)
        return list(groups.values())