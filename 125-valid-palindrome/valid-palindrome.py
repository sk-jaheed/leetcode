class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""
        for char in s:
            if char.isalnum():
                cleaned_string += char.lower()
        reversed_string = cleaned_string[::-1]
        if cleaned_string == reversed_string:
            return True
        else:
            return False
        