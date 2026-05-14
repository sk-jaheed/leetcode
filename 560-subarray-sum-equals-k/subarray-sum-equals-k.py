class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            if (current_sum - k) in hashmap:
                count += hashmap[current_sum - k]

            if current_sum in hashmap:
                hashmap[current_sum] += 1
            else:
                hashmap[current_sum] = 1

        return count
        