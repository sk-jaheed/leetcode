class Solution:
    def createTargetArray(self, nums, index):
        result = []
        for num,idx in zip(nums,index):
            result.insert(idx,num)
        return result
        