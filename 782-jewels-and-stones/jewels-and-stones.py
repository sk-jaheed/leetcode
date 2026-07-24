class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = Counter(stones)
        count = 0
        for char in jewels:
            if char in freq:
                count += freq[char]
        return count
        







#count = 0
       # for stone in stones:
          #  if stone in jewels:
              #  count += 1
      #  return count

        