class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortS = "".join(sorted(s))
        sortT = "".join(sorted(t))
        if sortT == sortS:
            return True
        return False