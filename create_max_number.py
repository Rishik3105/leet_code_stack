class Solution:
    def maxNumber(self, nums1, nums2, k):
      
        def maxSubsequence(nums, k):
            stack = []
            drop = len(nums) - k

            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(nums1, nums2):
            result = []
            while nums1 or nums2:
                if nums1 > nums2:
                    result.append(nums1.pop(0))
                else:
                    result.append(nums2.pop(0))
            return result
        best = []
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))
        for i in range(start, end + 1):
            part1 = maxSubsequence(nums1, i)
            part2 = maxSubsequence(nums2, k - i)
            candidate = merge(part1[:], part2[:])
            if candidate > best:
                best = candidate
        return best
