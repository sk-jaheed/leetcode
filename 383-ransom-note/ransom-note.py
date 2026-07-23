class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = Counter(magazine)
        for char in ransomNote:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        return True