class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        seen = {}
        for i,r in enumerate(list1):
            seen[r] = i
        result = []
        min_sum = float('inf')
        for j,r in enumerate(list2):
            if r in seen:
                total = seen[r] + j
                if total < min_sum:
                    min_sum = total
                    result = [r]
                elif total == min_sum:
                    result.append(r)
        return result
        