class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in range(k):
            if blocks[i] == "B":
                count += 1
        min_count = k - count
        for i in range(k,len(blocks)):
            if blocks[i-k] == "B":
                count -= 1
            if blocks[i] == "B":
                count  += 1
            min_count = min(min_count,k-count)
        return min_count
        
                                                             