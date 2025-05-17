class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 1, 2
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            i = nums[mid]
            if i == red:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif i == white:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
                