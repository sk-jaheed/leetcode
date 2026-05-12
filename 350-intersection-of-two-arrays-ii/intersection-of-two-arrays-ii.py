class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = Counter(nums1)
        result = []
        for num in nums2:
            if hashmap[num] > 0:
                result.append(num)
                hashmap[num] -= 1
        return result 

        