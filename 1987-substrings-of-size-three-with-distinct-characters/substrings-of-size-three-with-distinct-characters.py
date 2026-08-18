class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        if len(set(s[:3])) == 3:
            count += 1
        max_count = count
        for i in range(3,len(s)):
            if len(set(s[i-2:i+1])) == 3:
                count += 1
        return count
        