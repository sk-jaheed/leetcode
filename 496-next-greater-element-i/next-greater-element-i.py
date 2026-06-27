class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        hashmap = {}

        for num in reversed(nums2):

            while stack and stack[-1] <= num:
                stack.pop()

            if not stack:
                hashmap[num] = -1
            else:
                hashmap[num] = stack[-1]

            stack.append(num)

        ans = []

        for num in nums1:
            ans.append(hashmap[num])

        return ans