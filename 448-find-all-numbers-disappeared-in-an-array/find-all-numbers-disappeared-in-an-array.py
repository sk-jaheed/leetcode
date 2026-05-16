class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        result = []
        for i in range(1,len(nums)+1):
            if i not in hashmap:
                result.append(i)
        return result        