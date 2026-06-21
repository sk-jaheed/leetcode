class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # Convert non-digits into spaces
        cleaned_chars = [c if c.isdigit() else " " for c in word]
        
        # Join them back into a single string
        cleaned_string = "".join(cleaned_chars)
        
        # Split by spaces to isolate number groups, convert to int, and get unique count
        unique_ints = set(int(num) for num in cleaned_string.split())
        
        return len(unique_ints)

        