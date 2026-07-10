class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        soln: set[tuple] = set()

        for i in range(len(nums)):
            target = 0 - nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                elif s == target:
                    soln.add((nums[i], nums[left], nums[right]))
                    left += 1

        return [[*t] for t in soln]
