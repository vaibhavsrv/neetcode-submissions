class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = set(nums)

        if not nums:
            return 0

        best = 1

        for num in newNums:
            curr = num
            length = 1

            while curr + 1 in newNums:
                curr += 1
                length += 1
                
            best = max(best, length)
        return best