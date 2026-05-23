class Solution:
    def numIdenticalPairs(self, nums):
        hashmap = Counter(nums)
        pairs = 0
        for freq in hashmap.values():
            pairs += freq * (freq-1) // 2
        return pairs
        