class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        result = []
        for num in range(1,n+1):
            if num in target:
                stack.append(num)
                result.append("Push")
            else:
                stack.append(num)
                result.append("Push")
                stack.pop()
                result.append("Pop")
            if stack == target:
                break
        return result

        