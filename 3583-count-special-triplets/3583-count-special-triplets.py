class Solution(object):
    def specialTriplets(self, nums):
        """
        Count special triplets where nums[i] + nums[k] = nums[j] * 2
        
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        r = 0                    # total count
        rc = {}                  # right counter (elements ahead)
        
        # 🔄 STEP 1: Count all elements initially (everything is "right")
        for num in nums:
            if num in rc:
                rc[num] += 1
            else:
                rc[num] = 1
        
        lc = {}                  # left counter (elements behind)
        
        # 🔄 STEP 2: For each middle element j
        for j in range(n):
            target = nums[j] * 2  # what we need: i + k = j * 2
            
            # Remove current element from right side
            rc[nums[j]] -= 1
            
            # ✅ COUNT: left occurrences × right occurrences
            left_count = lc.get(target, 0)
            right_count = rc.get(target, 0)
            
            r += left_count * right_count
            
            # Add current element to left side
            if nums[j] in lc:
                lc[nums[j]] += 1
            else:
                lc[nums[j]] = 1
        
        return r % (10**9 + 7)