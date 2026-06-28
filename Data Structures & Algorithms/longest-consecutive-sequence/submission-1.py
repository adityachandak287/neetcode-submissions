class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        unq_nums = set(nums)

        curr = min(unq_nums)
        unq_nums.remove(curr)
        longest = 1
        curr_len = 1

        while unq_nums:
            if curr+1 in unq_nums:
                unq_nums.remove(curr+1)
                curr_len += 1
                longest = max(curr_len, longest)
                curr = curr+1
            else:
                curr = min(unq_nums)
                unq_nums.remove(curr)
                longest = max(curr_len, longest)
                curr_len = 1
        
        return longest
