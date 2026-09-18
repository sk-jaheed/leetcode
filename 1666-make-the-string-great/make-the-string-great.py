class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char.swapcase():
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
        #stack = []
        #for char in s:
         #   if char.isupper():
          #      if stack:
           #         stack.pop()
            #else:
             #   stack.append(char)
       # return "".join(stack)