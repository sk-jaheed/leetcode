class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        if not strs:
            return ""
        for char in zip(*strs):
            if len(set(char)) == 1:
                result.append(char[0])
            else:
                break
        return "".join(result)

        
        