class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s and t:
            word1 = sorted(s)
            word2 = sorted(t)
        else:
            return False
        if word1 == word2:
            return True
        else:
            return False
