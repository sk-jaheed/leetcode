class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        freq = Counter()
        answer = []
        for word in s1:
            freq[word] += 1
        for word in s2:
            freq[word] += 1
        for word in freq:
            if freq[word] == 1:
                answer.append(word)
        return answer


        