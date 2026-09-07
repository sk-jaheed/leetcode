class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        curr_sum = 0
        l = 0
        seen = set()
        result = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while nums[r] in seen:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
            seen.add(nums[r])
            result = max(result,curr_sum)
        return result
        