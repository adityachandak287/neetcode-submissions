class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = (l+r)//2

        if nums[l] < nums[r]:
            return nums[l]
        
        while nums[l] > nums[r]:
            if nums[l] <= nums[r]:
                return nums[l]
            
            elif nums[l] > nums[m]:
                r = m
            
            elif nums[m] > nums[r]:
                l = m+1
            
            m = (l+r)//2
        
        return nums[l]
