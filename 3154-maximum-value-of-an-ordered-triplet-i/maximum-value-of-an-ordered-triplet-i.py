class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triplet = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    value = (nums[i] - nums[j]) * nums[k]
                    max_triplet = max(max_triplet,value)
        return max_triplet
        