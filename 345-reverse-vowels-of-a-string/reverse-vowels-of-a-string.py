class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowel_list = []
        for ch in s:
            if ch in vowels:
                vowel_list.append(ch)
        vowel_list.reverse()
        result = []
        j = 0
        for ch in s:
            if ch in vowels:
                result.append(vowel_list[j])
                j += 1
            else:
                result.append(ch)
        return "".join(result)
# vowels = "aeiouAEIOU"
# s = list(s)
# left = 0
# right = len(s) - 1
# while left < right:
#     while left < right and s[left] not in vowels:
#           left += 1
#      while left < right and s[right] not in vowels:
#            right -= 1
#      s[left],s[right] = s[right],s[left]
#      left += 1
#      right -= 1
#      return "".join(s) 
