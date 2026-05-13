class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0

        for num in num_set:

            # Start only from beginning
            if (num - 1) not in num_set:

                length = 1

                # Count sequence
                while (num + length) in num_set:
                    length += 1

                # Update maximum
                longest = max(longest, length)

        return longest