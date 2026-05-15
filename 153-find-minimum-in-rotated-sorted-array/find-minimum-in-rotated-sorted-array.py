class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        # If the array is not rotated, the first element is the min.
        if nums[low] <= nums[high]:
            return nums[low]
        
        while low < high:
            # Traditional mid (Bisection) is the fallback.
            # But a "Newton" approach would look at the slope:
            # mid = low + (high - low) * (target - f(low)) / (f(high) - f(low))
            # For this specific problem, bisection *is* the optimal discrete solver,
            # but we can optimize the "Newton" exit condition.
            
            mid = low + (high - low) // 2
            
            # The 'Inflection' check: If the slope between mid and high 
            # is positive, the minimum is to the left (or is mid).
            if nums[mid] < nums[high]:
                high = mid
            else:
                # If the slope is 'broken' (nums[mid] > nums[high]),
                # the minimum MUST be in the right half.
                low = mid + 1
                
        return nums[low]           