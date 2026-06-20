class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones = 0
        max_zeros = 0
        
        current_ones = 0
        current_zeros = 0
        
        for char in s:
            if char == '1':
                current_ones += 1
                current_zeros = 0  # reset zeros
                max_ones = max(max_ones, current_ones)
            else:  # char == '0'
                current_zeros += 1
                current_ones = 0  # reset ones
                max_zeros = max(max_zeros, current_zeros)
        
        return max_ones > max_zeros