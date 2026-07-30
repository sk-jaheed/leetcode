class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""
        for char in s:
            if char.isalnum():
                cleaned_string += char.lower()
        reversed_string = ""
        for i in range(len(cleaned_string)-1,-1,-1):
            reversed_string += cleaned_string[i]
        if cleaned_string == reversed_string:
            return True
        else:
            return False
        