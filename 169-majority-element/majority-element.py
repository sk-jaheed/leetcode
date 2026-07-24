class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        freq = Counter(nums)
        return max(freq,key=freq.get)