class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            # If we encounter a 0, increase our zero tracker
            if nums[right] == 0:
                zero_count += 1
                
            # If we have more than one 0, shrink the window from the left
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
                
            # right - left dynamically calculates the window size minus the 1 skipped zero
            max_len = max(max_len, right - left)
            
        return max_len

