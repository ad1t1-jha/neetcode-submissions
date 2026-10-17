class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for i in strs:
            new = "".join(sorted(i))
            if new in words:
                words[new].append(i)
            else:
                words[new] = [i]
        result = []
        for i in words:
            result.append(words[i])
        return result
