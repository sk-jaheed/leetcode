class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for bro in operations:
            if "++" in bro:
                X += 1
            else:
                X -= 1
        return X
        