class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        p = 0
        app = -1 

        while p < n:
            if nums[p] == 1 and app == -1:
                app = p
            

            elif nums[p] == 1 and app != -1:
                d = p - app - 1
                app = p
                if d < k:
                    return False
            
            

            p += 1

        return True