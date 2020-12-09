"""
163. Missing Ranges
https://leetcode.com/problems/missing-ranges/
"""
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        prev = lower
        result = []

        if len(nums) == 0: 
            missing = upper - lower
            if missing == 0 : 
                result.append(str(lower))
            else: 
                result.append(str(lower) + "->" + str(upper))
            return result
            
        if nums[0] != lower:
            missing = nums[0] - lower
            if missing == 1 : 
                result.append(str(lower))
            else: 
                result.append(str(lower) + "->" + str(nums[0] - 1))
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev + 1:
                missing = nums[i] - prev
                if missing == 2 : 
                    result.append(str(prev + 1))
                else: 
                    result.append(str(prev+1) + "->" + str(nums[i] - 1))
            prev = nums[i]
        if nums[-1] != upper:
            missing = upper - nums[-1]
            if missing == 1 : 
                result.append(str(upper))
            else: 
                result.append(str(nums[-1]+1) + "->" + str(upper))
        return result        
                
