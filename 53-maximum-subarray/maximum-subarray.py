class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarr = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum = curr_sum + num
            if curr_sum > max_subarr:
                max_subarr = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_subarr
