class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        p_to_w = {}
        w_to_p = {}
        if len(pattern) != len(words):
            return False
        for char,word in zip(pattern,words):
            if char in p_to_w:
                if p_to_w[char] != word:
                    return False
            if word in w_to_p:
                if w_to_p[word] != char:
                    return False
            p_to_w[char] = word
            w_to_p[word] = char
        return True

        