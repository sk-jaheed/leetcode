class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        altitude = 0
        for high in gain:
            altitude += high
            max_alt = max(max_alt,altitude)
        return max_alt        