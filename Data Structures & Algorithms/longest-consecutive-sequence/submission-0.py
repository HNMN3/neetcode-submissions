from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        sequence_dict = defaultdict(int)
        max_sequence = 1
        sequence = 1
        i = 1
        l = len(nums)
        while i < l:
            if nums[i] == nums[i-1]:
                pass
            elif nums[i] == nums[i-1] + 1:
                sequence += 1
            else:
                max_sequence = max(max_sequence, sequence)
                sequence = 1
            i += 1

        return max(max_sequence, sequence)
        