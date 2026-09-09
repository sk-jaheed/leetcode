class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l,r,falsecount,truecount,result = 0,0,0,0,0
        n = len(answerKey)
        while r < n:
            if answerKey[r] == 'T':
                truecount += 1
            if answerKey[r] == 'F':
                falsecount += 1
            while truecount > k and falsecount > k:
                if answerKey[l] == 'T':
                    truecount -= 1
                if answerKey[l] == 'F':
                    falsecount -=  1
                l += 1
            result  = max(result, r - l + 1)
            r += 1
        return result

        