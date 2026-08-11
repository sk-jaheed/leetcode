class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]


    #   seen = {}
       # for i in range(len(nums)):
       #     need = target - nums[i]
        #    if need in seen:
         #       return[seen[need],i]
          #  seen[need[i]] = i