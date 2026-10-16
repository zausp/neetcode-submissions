class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            temp = "".join(sorted(string))
            seen.setdefault(temp, []).append(string)
        return list(seen.values())
            