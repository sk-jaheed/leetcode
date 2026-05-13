class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        window_count = Counter(s[:len(p)])
        result = []
        if window_count == p_count:
            result.append(0)
        for i in range(len(p),len(s)):
            left = s[i-len(p)]
            window_count[left] -= 1
            right = s[i]
            window_count[right] +=1
            if window_count == p_count:
                result.append(i-len(p)+1)
        return result
        