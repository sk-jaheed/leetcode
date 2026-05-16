class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        duplicate = 0
        missing = 0
        for i in range(1,len(nums)+1):
            if hashmap[i] > 1:
                duplicate = i
            if hashmap[i] == 0:
                missing = i
        return[duplicate,missing]
  