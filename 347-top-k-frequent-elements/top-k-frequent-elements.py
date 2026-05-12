class Solution:
    def topKFrequent(self, nums, k):
        hashmap = Counter(nums)
        result  = []
        for pair in hashmap.most_common(k):
            result.append(pair[0])
        return result
        